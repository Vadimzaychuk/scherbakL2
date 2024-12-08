from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    today = datetime.now().strftime("%A, %d %B %Y")  
    return render_template("index.html", date=today)

if __name__ == "__main__":
    app.run(debug=True)
