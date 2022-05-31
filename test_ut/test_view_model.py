from pickle import TRUE
from todo_app.app import ViewModel
from todo_app.data.trello_items import Item


test_items = [Item('Item1', 'Item 1', 'To Do'),Item('Item2', 'Item 2', 'Completed'),Item('Item3', 'Item 3', 'Doing') ]
a = ViewModel(test_items)


def test_todo_items():
    return_list = a.todo_items
    for x in return_list:
     assert x.status == 'To Do'  


def test_doing_items():
    return_list1 = a.doing_items
    for x in return_list1:
     assert x.status == 'Doing'   
    

def test_completed_items():
    return_list2 = a.completed_items
    for x in return_list2:
     assert x.status == 'Completed'   


