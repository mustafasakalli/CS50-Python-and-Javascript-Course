from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Sürgün", "İsveç", "Lordu", "Yüce", "Sakal", "Haşmetmeapları"]
    return render_template("index.html", names=names)
