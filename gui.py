import FreeSimpleGUI as sg
import functions


label = sg.Text("Type in a ToDo")
input_box = sg.InputText(tooltip="Enter ToDo")
add_button = sg.Button("Add Item")

window = sg.Window('My ToDo App',layout=[[label],[input_box, add_button]])
window.read()
window.close()