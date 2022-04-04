import os

import waitress
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Congratulations, it's a web app!"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33507))
    waitress.serve(app,port=port)
