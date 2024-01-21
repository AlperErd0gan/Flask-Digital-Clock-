from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_time")
def get_time():
    return time.strftime("%H:%M:%S")

if __name__ == "__main__":
    app.run(debug=True)

