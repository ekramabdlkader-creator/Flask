from flask import Flask
app=Flask(__name__) 
@app.route("/product/<string:name>/<int:id>/<float:price>/<path:file>")
def product(name,id,price,file):
    return f" name: {name} , id :{id}  , price: {price} , file ;{ file} "
if __name__=="__main__":
    app.run(debug=True)
