import uuid
from datetime import datetime
from io import BytesIO

import db
from excel_parser import parse


def process_file(data):
    result = parse(BytesIO(data))
    # TODO: Получение имени загружаемого файла
    result['name'] = ''
    result['timestamp'] = datetime.now().strftime('%Y-%m-%d-%H.%M.%S')
    result['uuid'] = uuid.uuid4().hex
    db.insert(result)
    return result
