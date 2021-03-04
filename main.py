from flask import Flask, render_template, request, redirect, url_for
from src.database import Database
import secrets

app = Flask(__name__, static_folder="static/", static_url_path="/static", template_folder="templates/")

db = Database("miniurl.db")

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        long_url = request.form["miniurl"]
        short_url_id = generate_unique_url_id()
        db.insert_url(long_url, short_url_id)
    
        return render_template('minishort.html', short_url_display=f"{short_url_id}", title="Minimal URL")
    else:
        #new_url = Url(long_url, short_url_id)
        #create short url if not found
        return render_template('index.html', title='Minimal Url')

# 127.0.0.1:5000/u/l8w9sA
@app.route('/<url_id>', methods=['GET'])
def redirect_url(url_id):
    long_url = db.get_long_url(url_id)
    return redirect(long_url[0])

def generate_unique_url_id():
    url_id = secrets.token_urlsafe(4)
    if db.url_id_exists(url_id):
        return generate_unique_url_id()
    else:
        return url_id

if __name__ == "__main__":
    app.run()