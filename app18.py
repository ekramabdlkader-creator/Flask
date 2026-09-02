from flask import Flask ,request
app=Flask(__name__)
@app.route("/student",methods=["GET"])
def student():
    name=request.args.get("name")
    age=request.args.get("age")
    department=request.args.get("department")
    return f" name: {name} ,age: {age} ,  department: {department}"
if __name__=="__main__":
    app.run(debug=True)