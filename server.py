
from flask import Flask, render_template, request, jsonify
from handlers.upload import process_file

PORT = 2016
app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/upload/', methods=['POST'])
def upload_resource():
    if request.method == 'POST':
        result = process_file(request.data)
        return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=PORT)
