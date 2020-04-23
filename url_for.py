from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    return redirect(url_for('hello', 'aaa'))


@app.route('/hello/aaa')
def hello(username):
    return hello


if __name__ == '__main__':
    app.debug = True
    app.run()
