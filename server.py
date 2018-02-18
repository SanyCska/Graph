from tinydb import TinyDB
from flask import Flask, render_template, request, jsonify, send_from_directory
import json
from werkzeug.utils import secure_filename

from handlers.upload import process_file
import db

PORT = 2016
app = Flask(__name__, static_url_path='', static_folder = "static")

@app.route('/')
def index_page():
    return render_template('index.html')

app.config["UPLOAD_FOLDER"] = "uploads"


@app.route('/upload/', methods=['POST'])
def upload_resource():
    if request.method == 'POST':
        print('zbc')
        file = request.files.to_dict().get('file')
        print(file.filename)
        process_file(file.read(), file.filename)
        return 'success'


@app.route('/graphs/')
def graphs():
    return jsonify({
        'graphs': db.graphs()
    })


@app.route('/graphs/<graph_uid>/')
def graph(graph_uid):
    return jsonify(db.read(graph_uid))


@app.route('/selected_graph/', methods=['POST'])
def selected_graph():
    graph_uuid = request.form.to_dict().get('data', '')
    return(graph_uuid)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)

