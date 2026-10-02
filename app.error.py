from flask import Flask,jsonify
app=Flask(__name__)
products=[
    {"id": 1,"name":"Laptop"},
    {"id":2 ,"name": "Phone"}
]
@app.route("/product/<int:id>" , methods=["GET"])
def get_product(id):
    for product in products:
        if product["id"]== id:
            return jsonify(product),200
        return jsonify({"error":"product not found"}) ,404
if __name__=="__main__":
        app.run(debug=True)