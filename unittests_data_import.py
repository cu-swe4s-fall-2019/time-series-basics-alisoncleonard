"""
unit tests for data_import.py class ImportData
"""
import unittest
import data_import


class TestLinearSearch(unittest.TestCase):
    def test_linear_search_one_hit(self):

        self._roundtimeStr = [1, 2, 3, 4, 5, 6]
        self._value = [4, 6, 5, 8, 6, 7]

        r = data_import.ImportData.linear_search_value(self, 3)
        self.assertEqual(r, [5])

    def test_linear_search_several_hits(self):

        self._roundtimeStr = [1, 2, 3, 4, 3, 6]
        self._value = [4, 6, 5, 8, 6, 7]

        r = data_import.ImportData.linear_search_value(self, 3)
        self.assertEqual(r, [5, 6])

    def test_linear_search_not_found(self):

        self._roundtimeStr = [1, 2, 3, 4, 5, 6]
        self._value = [4, 6, 5, 8, 6, 7]

        r = data_import.ImportData.linear_search_value(self, 10)
        self.assertEqual(r, [])

    def test_linear_search_floats(self):

        self._roundtimeStr = [1.4, 2.2, 3.5, 4.6, 5.3, 6.9]
        self._value = [4.4, 6.3, 5.7, 8.8, 6.5, 7.1]

        r = data_import.ImportData.linear_search_value(self, 3.5)
        self.assertEqual(r, [5.7])

class TestroundTime(unittest.TestCase):
    def test_roundTime_basic(self):
        pass


if __name__ == '__main__':
    unittest.main()
