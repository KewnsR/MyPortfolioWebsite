from flask import Flask, render_template
import os

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    return render_template("index.html")

# About
@app.route("/about")
def about():
    return render_template("about.html")

# Projects
@app.route("/projects")
def projects():
    return render_template("projects.html")

# Contact
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
