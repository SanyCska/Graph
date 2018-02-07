from tinydb import TinyDB
from flask import Flask, render_template, request, jsonify

from handlers.upload import process_file
import db

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


@app.route('/graphs/')
def graphs():
    return jsonify({
        'graphs': db.graphs()
    })

@app.route('/graphs/<graph_uid>/')
def graph(graph_uid):
    return jsonify(db.read(graph_uid))

if __name__ == '__main__':
    app.run(debug=True, port=PORT)
