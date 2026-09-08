from flask import Flask ,jsonify
app=Flask(__name__)
students={ "id": 1, "name": "Ekram", "department": "IT" ,
          "id":2 ,"name": "Rifat", "department": "CS"    

          }
@app.route("/student" ,methods=["GET"])
def get_students():
    return jsonify(students)
if __name__=="__main__":
    app.run(debug=True)
