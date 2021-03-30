from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")

@app.route("/enn")
def enn():
    return render_template("enn.html")

@app.route("/kekka")
def kekka():
    e = int(request.args.get("en"))
    r = (e+e)*3.14
    m = e*e*3.14
    return render_template("kekka.html",r=r,m=m)

if __name__ == "__main__":
    app.run(debug=True)