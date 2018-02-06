from flask import Flask, render_template
from output import take_data
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    print(take_data())
    app.run(port=2016)