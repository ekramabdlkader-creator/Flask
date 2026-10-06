from flask import Flask ,render_template
app=Flask(__name__)
@app.route("/")
def  home():
    students=["Ekram","Muna","Rifat"]
    return render_template("list.html",Students=students)
if __name__=="__main__":
    app.run(debug=True)