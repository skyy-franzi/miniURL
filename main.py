from flask import Flask, render_template, request
from src.database import Database
import secrets

app = Flask(__name__, static_folder="static/", static_url_path="/static", template_folder="templates/")

db = Database("miniurl.db")

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        get_url = request.form["miniurl"]
        short_url = secrets.token_urlsafe(4)
        db.insert_url(get_url, short_url)
        # check if url already exists
        # return short url if found
        return get_url
    else:
        #create short url if not found
        return render_template('index.html', title='Minimal Url')

