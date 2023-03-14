from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/getName')
def hello_world():  # put application's code here
    return 'my name is lucy!'


if __name__ == '__main__':
    app.run()
