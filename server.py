from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def macro():
    return render_template("index.html")

@app.route("/year")
def micro():
    return render_template("year.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
