from flask import Flask
from flask import render_template
from data import get_chars

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        'index.html'
    )


@app.route("/template")
def template():
    return render_template(
        'template.html',
        chars=get_chars()
    )

if __name__ == "__main__":
    app.run(debug=True)