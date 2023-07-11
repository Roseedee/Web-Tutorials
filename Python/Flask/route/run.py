from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<center><h1>Home Page</h1></center>"

@app.route("/about")
def about():
    return "<center><h1>About Page</h1></center>"

@app.route("/profile")
def profile():
    return "<center><h1>Profile Page</h1></center>"


if __name__ == "__main__":
    app.run()