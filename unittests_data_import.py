"""
unit tests for data_import.py class ImportData
"""
import unittest
import data_import

# how do you write unit tests for functions in a class?

class TestImportData(unittest.TestCase):
    def test_linear_search(self):

        self._roundtimeStr = [1, 2, 3, 4, 5, 6]

        r = data_import.ImportData.linear_search_value(self, 3)
        self.assertEqual(r, [2]) # the index where 3 occurs in L

    def test_linear_search_not_found(self):

        self._roundtimeStr = [1, 2, 3, 4, 5, 6]

        r = data_import.ImportData.linear_search_value(self, 10)
        self.assertEqual(r, [])

if __name__ == '__main__':
    unittest.main()
