import read_file as rv
import unittest

def test_files():
    
    file_test = []
    
    txt = rv.read_data_file('numbers.txt')
    csv = rv.read_data_csv('more_numbers.csv')
    
    file_test.append(txt)
    file_test.append(csv)
    
    return file_test

class TestFiles(unittest.TestCase):
    
    def test_read_file(self):
        file_test = test_files()
        self.assertEqual(file_test[0], [1, 3, 99, 100, 120, 32, 330, 23, 76, 44, 31])
        self.assertEqual(file_test[1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit = False, verbosity = 3)
