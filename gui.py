import os.path
import time

import FreeSimpleGUI as sg
import functions

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass

sg.theme('DarkPurple4')
clock = sg.Text('',key='clock')
label = sg.Text("Type in a ToDo")
input_box = sg.InputText(tooltip="Enter ToDo", key="todo")
add_button = sg.Button("Add Item")
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My ToDo App',
                   layout=[[clock],
                        [label],[input_box, add_button],
                        [list_box, edit_button, complete_button],
                        [exit_button]],
                   font=('Helvetica',20))

while True:
    event, values = window.read(timeout=1000)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values['todo'])
    match event:
        case "Add Item":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item.", font=('Helvetica',20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item.", font=('Helvetica',20))
        case "Exit":
            break
        case "todos":
            try:
                window['todo'].update(value=values['todos'][0])
            except IndexError:
                sg.popup("Please select an item.", font=('Helvetica',20))
        case sg.WIN_CLOSED:
            break


window.close()