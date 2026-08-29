from flask import Flask
app=Flask(__name__)
@app.route("/student/<name>/<int:id>")
def student(name,id):
    return f" my is {name} , the id number is ,{id}"
if __name__=="__main__":
    app.run(debug=True)