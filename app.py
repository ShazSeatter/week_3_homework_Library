from flask import Flask

app = Flask(__name__)

from controller import controller

if __name__ == "__main__":
    app.run()