from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET", "POST"])
def hello():
    name = None
    if request.method == "POST":
        name = request.form.get("name", "").strip() or None
    return render_template("hello.html", name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5000)
    

