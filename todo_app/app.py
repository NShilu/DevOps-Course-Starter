from flask import Flask, redirect, url_for, request
from flask import render_template

from todo_app.flask_config import Config
from todo_app.data.session_items import add_item
from todo_app.data.trello_items import get_items


app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template("index.html", items = items)

@app.route('/addItem', methods=['POST'])
def add_item():
    title=request.form.get('title')
    add_item(title)
    return redirect('/')

    

