from flask import Flask, session, redirect, url_for, request
from flask.templating import render_template

from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items, add_item, complete_card


class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items    
    
    @property
    def todo_items(self):
        to_do_items_list=[]  
        for item in self._items:
            if item.status =="To Do":
                 to_do_items_list.append(item)
        return to_do_items_list

    @property
    def doing_items(self):
        doing_items_list=[]
        for item in self._items:
         if item.status =="Doing":
             doing_items_list.append(item)
        return doing_items_list

    @property
    def completed_items(self):
        completed_items_list=[]
        for item in self._items:
         if item.status =="Completed":
             completed_items_list.append(item)
        return completed_items_list    

                                             
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
                        

    #Show the index page template    
    @app.route('/')
    def index():
        items=get_items()
        item_view_model = ViewModel(items)
        return render_template('index.html',view_model=item_view_model)



    #Create new todo items    
    @app.route('/addItem', methods=['POST'])
    def index_addItem():
        title=request.form.get('title')
        add_item(title)
        return redirect('/')

        
    @app.route('/completeItem',methods=['POST'])
    def complete_item():
        Listid=request.form.get('ItemID')
        complete_card(Listid)
        return redirect('/')
    return app       