from flask import Flask
from flask import make_response
from flask import render_template
from pdfkit import from_string
from data import get_chars

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        'index.html'
    )


@app.route("/template")
def template():
    html = render_template(
        'template.html',
        chars=get_chars()
    )
    pdf = from_string(html, False, css='static/template.css')
    response = make_response(pdf)
    response.headers['Content-Disposition'] = "filename=template.pdf"
    response.mimetype = 'application/pdf'
    return response

if __name__ == "__main__":
    app.run(debug=True)
