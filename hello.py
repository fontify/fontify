import os
import subprocess
import tempfile
from time import sleep
from flask import Flask
from flask import request
from flask import send_from_directory
from flask import make_response
from flask import render_template
from flask import jsonify
from pdfkit import from_string
from data import get_chars
from data import get_sample_chars
from data import TMPL_OPTIONS

UPLOAD_FOLDER = '../upload'
DOWNLOAD_FOLDER = '../download'
FONT_NAME = 'fontify.ttf'
ALLOWED_EXTENSIONS = set(['jpg', 'png', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['FONT_NAME'] = FONT_NAME


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/finish")
def finish():
    key = request.args.get('key')
    return render_template(
        'finish.html',
        url=key + '/' + app.config['FONT_NAME']
    )


@app.route("/template")
def template():
    html = render_template(
        'template.html',
        chars=get_chars(),
        sample=get_sample_chars()
    )
    pdf = from_string(
        html,
        False,
        options=TMPL_OPTIONS,
        css='static/template.css'
    )
    response = make_response(pdf)
    response.headers['Content-Disposition'] = "filename=template.pdf"
    response.mimetype = 'application/pdf'
    return response


@app.route("/download/<key>/<fontname>")
def download(key, fontname):
    return send_from_directory(
        os.path.join(app.config['DOWNLOAD_FOLDER'], key),
        fontname
    )


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/upload-file", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            _, ext = os.path.splitext(file.filename)
            f, filename = tempfile.mkstemp(
                prefix='',
                suffix=ext,
                dir=app.config['UPLOAD_FOLDER']
            )
            file.save(filename)
            font_name = request.form['font-name']
            key = filename.split('/')[-1].split('.')[0]
            subprocess.call(["python", "scripts/fontify.py", "-n", font_name, "-o", app.config['UPLOAD_FOLDER'] + "/" + key + "/" + "fontify.ttf", filename])
            return jsonify(font_name=font_name, key=key)
    return ''

if __name__ == "__main__":
    app.run(debug=True)
