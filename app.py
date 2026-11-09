from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("blue.html")


@app.get("/about")
def about():
    return render_template("about.html")


@app.get("/housing")
def housing():
    return render_template("housing.html")


@app.get("/meals")
def meals():
    return render_template("meals.html")


@app.get("/alternate")
def alternate():
    return render_template("alternate.html")


@app.get("/blue")
def blue():
    return home()


if __name__ == "__main__":
    app.run(debug=True)
