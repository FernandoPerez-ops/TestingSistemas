import unittest
from unittest.mock import patch
from Parcial_1 import get_info, promediacion

class TestGetData(unittest.TestCase):
    mocks = { 'ejemplo': [['hotmail.com', 85], 
                       ['hotmail.com', 75],     
                       ['gmail.com', 90], 
                       ['outlook.com', 74], 
                       ['gmail.com', 88], 
                       ['hotmail.com', 92]],

               'ejemplo2': [['pornhub.com', 100],
                        ['xnxx.com', 92],
                        ['pornhub.com', 91],
                        ['xnxx.com', 80],
                        ['pornhub.com', 76]],

                'ejemplo3': [['camntasia.com', 80],
                        ['camntasia.com', 60],
                        ['gmx.com', 70],
                        ['new.com', 90],
                        ['camntasia.com', 70],
                        ['gmx.com', 100],
                        ['new.com', 90]],
            }
    
    @patch("parcial_1.get_info", return_value = mocks['ejemplo'])
    def test_separacionypromediacion(self, mock_get):
        salida_esperada = promediacion()
        salida_real = [['hotmail.com', 84.0], ['gmail.com', 89.0], ['outlook.com', 74.0]]
        self.assertEqual(salida_real, salida_esperada)
    
    @patch("parcial_1.get_info", return_value = mocks['ejemplo2'])
    def test_separacionypromediacion2(self, mock_get):
        salida_esperada = promediacion()
        salida_real = [['pornhub.com', 89.0], ['xnxx.com', 86.0]]
        self.assertEqual(salida_real, salida_esperada)
    
    @patch("parcial_1.get_info", return_value = mocks['ejemplo3'])
    def test_separacionypromediacion3(self, mock_get):
        salida_esperada = promediacion()
        salida_real = [['camntsia.com', 70.0], ['gmx.com', 85.0], ['new.com', 90.0]]
        self.assertEqual(salida_real, salida_esperada)
        
if __name__ == '__main__':
    unittest.main()