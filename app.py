from flask import Flask

app = Flask(__name__)

"""git 分支切换"""


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
