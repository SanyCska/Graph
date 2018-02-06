from datetime import datetime
from io import BytesIO

from flask import Flask, render_template, request, jsonify

from excel_parser import parse

PORT = 2016
app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/upload/', methods=['POST'])
def upload_resource():
    if request.method == 'POST':
        result = parse(BytesIO(request.data))
        # TODO: Получение имени загружаемого файла
        result['name'] = ''
        result['timestamp'] = datetime.now().strftime('%Y-%m-%d-%H.%M.%S')
        return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=PORT)
