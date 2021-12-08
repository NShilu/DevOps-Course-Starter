from flask import Flask, redirect, url_for, request
from flask import render_template

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template("index.html", items = items)

@app.route('/addItem', methods=['POST'])

def index_addItem():

    title=request.form.get('title')

    add_item(title)

    return redirect('/')

