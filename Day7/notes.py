from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

shared_content = "" 

@app.route("/", methods=["GET"])
def option():
    global shared_content
    return render_template("home.html", content=shared_content)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    global shared_content
    if request.method == "POST":
        shared_content = request.form.get('content', "") 
    return render_template("update.html", content=shared_content)

@app.route("/admin/clearnotes", methods=["GET"])
def clear():
    global shared_content
    shared_content = ""  
    return redirect(url_for("option"))  

if __name__ == "__main__":
    app.run(debug=True)