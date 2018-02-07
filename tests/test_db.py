import unittest
import uuid

import db


class TestLoader(unittest.TestCase):

    def test_db(self):
        data_uuid = uuid.uuid4().hex
        data = {
            'name': '',
            'branches': [
                (1, 2),
                (2, 3),
                (3, 4),
                (4, 1),
                (2, 5),
                (1, 5)
            ],
            'nodes': [1, 2, 3, 4, 5],
            'uuid': data_uuid
        }

        db.insert(data)
        db_data = db.read(data_uuid)

        expected = [{
            'name': '',
            'branches': [
                [1, 2],
                [2, 3],
                [3, 4],
                [4, 1],
                [2, 5],
                [1, 5]
            ],
            'nodes': [1, 2, 3, 4, 5],
            'uuid': data_uuid

        }]

        self.assertListEqual(db_data, expected)
