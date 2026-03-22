from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Om meg")

@app.route("/about")
def about():
    return render_template("about.html", title="Om Flask")

if __name__ == "__main__":
    app.run(debug=True)