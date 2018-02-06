import unittest

from excel_parser import parse


class TestLoader(unittest.TestCase):

    def test_load(self):
        result = parse('../upload/test1.xlsx')
        expected = {
            'branches': [
                (1, 2),
                (2, 3),
                (3, 4),
                (4, 1),
                (2, 5),
                (1, 5)
            ],
            'nodes': {1, 2, 3, 4, 5}
        }
        self.assertDictEqual(result, expected)
