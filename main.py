from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__, static_folder="static/", static_url_path="/static", template_folder="templates/")

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        get_url = request.form["miniurl"]
        return get_url
    else:
        return render_template('index.html', title='Minimal Url')

