from flask import Flask,render_template,request,url_for,redirect,flash

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/astillero")
def astillero():
    return render_template("astillero.html")

@app.route("/castillo")
def castillo():
    return render_template("castillo.html")

@app.route("/catedral")
def catedral():
    return render_template("catedral.html")

@app.route("/santuario")
def santuario():
    return render_template("santuario.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)