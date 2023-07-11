from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<center><h1>Home Page</h1></center>"

@app.route("/about")
def about():
    return "<center><h1>About Page</h1></center"

#sample url : localhost:5000/profile/"enter your name"
@app.route("/profile/<yourName>")
def profile(yourName):
    return "<center><h1>Profile Page</h1><h2>Welcome : {}</h2></center>".format(yourName)

if __name__ == "__main__":
    app.run()