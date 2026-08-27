from flask import Flask
app=Flask(__name__)
@app.route("/product/<name>/<price>")
def product(name,price):
    return f"hello ,{name} ,your product price is  {price}"
if __name__=="__main__":
    app.run(debug=True)