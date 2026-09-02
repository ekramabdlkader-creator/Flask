from flask import Flask ,request
app=Flask(__name__)
@app.route("/product",methods=["GET"])
def product():
    name=request.args.get("name")
    price=request.args.get("price")
    catagory=request.args.get("catagory")
    return f" Name: {name} , price: {price} , catagory: {catagory}"
if __name__=="__main__":
    app.run(debug=True)