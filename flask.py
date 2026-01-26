from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "home page"
@app.route("/login")
def login():
    return "login page"
@app.route("/deshboard")
def deshboard():
    return "deshboard page"
if __name__ == "__main__":
    app.run(debug=True)