from flask import Flask ,request,jsonify
app=Flask(__name__)
@app.route("/student")
def student():
 students ={ "mame":"Ekram",
           "age":21,
           "department" :"IT"}
 return  jsonify(students)
if __name__=="__main__":
 app.run(debug=True)
 
