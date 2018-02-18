import uuid
from datetime import datetime
from io import BytesIO

import db
from excel_parser import parse


def process_file(data, name):
    result = parse(BytesIO(data))
    result['name'] = name
    result['timestamp'] = datetime.now().strftime('%Y-%m-%d-%H.%M.%S')
    result['uuid'] = uuid.uuid4().hex
    db.insert(result)
    return result
