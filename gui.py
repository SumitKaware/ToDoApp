import FreeSimpleGUI as sg
import functions


label = sg.Text("Type in a ToDo")
input_box = sg.InputText(tooltip="Enter ToDo", key="todo")
add_button = sg.Button("Add Item")
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window('My ToDo App',
                   layout=[[label],[input_box, add_button],
                           [list_box, edit_button
                            ]],
                   font=('Helvetica',20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todo'])
    match event:
        case "Add Item":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case sg.WIN_CLOSED:
            break


window.close()