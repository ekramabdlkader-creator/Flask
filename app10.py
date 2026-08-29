from flask import Flask
app=Flask(__name__)
@app.route("/user/<name>/<int:age>")
def user(name,age):
    return f"  hello {name} , you are  {age} years old" 
if __name__=="__main__":
    app.run(debug=True)