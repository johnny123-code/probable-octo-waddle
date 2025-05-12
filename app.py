from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(entry):
    data = load_data()
    data.append(entry)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    stories = load_data()
    return render_template("index.html", stories=stories)

@app.route('/submit', methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form.get("name", "Anonymous")
        message = request.form.get("message", "")
        if message:
            save_data({"name": name, "message": message})
        return redirect(url_for("index"))
    return render_template("submit.html")

@app.route('/resources')
def resources():
    return render_template("resources.html")

if __name__ == "__main__":
    app.run(debug=True)
