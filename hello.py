import os
import subprocess
from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import send_from_directory
from flask import make_response
from flask import render_template
from pdfkit import from_string
from data import get_chars
from data import get_sample_chars
from data import TMPL_OPTIONS
from werkzeug import secure_filename

UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = set(['jpg', 'png'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template(
        'index.html'
    )


@app.route("/finish")
def finish():
    return render_template(
        'finish.html'
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


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/upload-file", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print filename
            print url_for('uploaded_file', filename=filename)
            subprocess.call(["ls", "-l"])
            return redirect(url_for('uploaded_file', filename=filename))
    return ''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == "__main__":
    app.run(debug=True)
