from flask import Flask
from flask import render_template
import os

app = Flask(__name__)
directory = os.getcwd()


@app.route('/')
def index():
    return render_template('index.html')
    # return directory


if __name__ == '__main__':
    app.debug = True
    app.run()
