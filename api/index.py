from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../templates')

teachers_data = [
    {"name": "楊子青", "lab": "579"},
    {"name": "楊子青2", "lab": "579"},
    {"name": "楊子青3", "lab": "999"}
]

@app.route("/", methods=["GET", "POST"])
@app.route("/search", methods=["GET", "POST"])
def search():
    keyword = ""
    results = []
    if request.method == "POST":
        keyword = request.form.get("keyword", "")
        if keyword:
            results = [t for t in teachers_data if keyword in t["name"]]
    return render_template("search.html", keyword=keyword, results=results)

app.debug = True