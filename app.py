from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!5 why not???"
