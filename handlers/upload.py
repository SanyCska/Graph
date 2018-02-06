from datetime import datetime
from io import BytesIO

from excel_parser import parse


def process_file(data):
    result = parse(BytesIO(data))
    # TODO: Получение имени загружаемого файла
    result['name'] = ''
    result['timestamp'] = datetime.now().strftime('%Y-%m-%d-%H.%M.%S')
    # TODO: Запись в БД
    return result
