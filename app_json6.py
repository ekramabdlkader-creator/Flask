from flask  import Flask ,request,jsonify
app=Flask(__name__)
students=[
    { " name":"Ekram" ,"age":21},
    {"name":"MUNA" ,"age":12}
]
@app.route("/students" ,methods=["POST"])
def create_students():
    data=request.get_json()
    name=data["name"]
    age=data["age"]
    students.append({
        "name":name,
        "age":age
    })
    return jsonify(students)
if __name__=="__main__":
    app.run(debug=True)
    

