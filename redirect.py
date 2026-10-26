from flask import Flask,render_template,request,redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/about")
def about():
    return "This is About Page"

@app.route("/submit" ,methods=["POST"])
def submit():
    name=request.form.get("name" ,"").strip()
    department=request.form.get("department" ,"").strip
    if not name or not department:
        return redirect(url_for("home"))
    
    return render_template("result.html",
                            name=name ,
                            department=department)


if __name__=="__main__":
    app.run(debug=True)