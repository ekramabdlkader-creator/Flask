#multiple rooutes in  one application 
from flask import Flask 
app=Flask(__name__)
@app.route("/")
def home():
    return f"Hello, World!"
@app.route("/about")
def about():
    return f"this is my about page"
@app.route("/student")
def student():
    return f"Hello, Student!"
@app.route("/greeting")
def greeting():
    return f"Hello, there!"

if __name__=="__main__":
    app.run(debug=True)