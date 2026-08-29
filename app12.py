from flask import Flask, app 
app=Flask(__name__)
@app.route("/product/<name>/<int:price>/<catagory>")
def product(name,price,catagory):
    return f"product: { name}  , price : {price} ,catagory: {catagory}"
if __name__=="__main__":
    app.run(debug=True) 