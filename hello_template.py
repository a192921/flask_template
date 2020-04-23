from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/<user>')
def index(user):
    return render_template('hello.html', user_template=user)


if __name__ == "__main__":
    app.run(debug='True')
