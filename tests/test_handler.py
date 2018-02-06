import unittest
from handlers.upload import process_file


class TestLoader(unittest.TestCase):

    def test_load(self):

        with open('../upload/test1.xlsx', 'rb') as f:
            result = process_file(f.read())
        del result['timestamp']

        expected = {
            'name': '',
            'branches': [
                (1, 2),
                (2, 3),
                (3, 4),
                (4, 1),
                (2, 5),
                (1, 5)
            ],
            'nodes': [1, 2, 3, 4, 5]

        }
        self.assertDictEqual(result, expected)
