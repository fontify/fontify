# Fontify
Make your own typeface from your handwriting!

## Development

First clone and `cd` into the repository.

Install wkhtmltopdf: http://wkhtmltopdf.org/downloads.html

```shell
npm install -g ttf2woff

virtualenv env
source env/bin/activate
pip install -r requirements.txt
python hello.py

git submodule init
git submodule update
# install fontforge
# install opencv
# install cv2 (opencv binding for Python)
```
