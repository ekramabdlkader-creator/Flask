from flask import Flask ,request
app=Flask(__name__)
@app.route("/student")
def student():
    name=request.args.get("name")
    age=request.args.get("age")
    return f"Namee: { name} ,Age :{age} "
if __name__=="__main__":
    app.run(debug=True)
