import datetime
from crypt import methods
from flask import Flask, render_template, request

app = Flask(__name__)

entries = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        date = datetime.datetime.today().strftime("%Y-%-m-%d")
        entries.append((entry_content, date))
      
    
    return render_template("home.html", entries=entries)


if __name__=="__main__":
    app.run(debug = True)