import os
from flask import Flask, request, redirect, url_for, render_template
from pdfkit import from_string
from data import get_chars
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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/file-upload", methods=['POST'])
def file_upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file',
                                    # filename=filename))
            return "save sucess"
    return "lalala"


if __name__ == "__main__":
    app.run(debug=True)
