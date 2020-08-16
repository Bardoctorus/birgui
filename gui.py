import PySimpleGUI as sg
import image_resize as ir

sg.theme('BluePurple')

layout = [[sg.Text('Choose a folder')],
          [sg.Text('File 1', size=(8, 1)), sg.Input(key='-FOLDERPATH-'), sg.FolderBrowse()],
          [sg.Text('Choose new width for images')],
          [sg.Text('File 2', size=(8, 1)), sg.Input(key='-SIZE-')],
          [sg.Text(' '), sg.Text(size=(80,1), key='-OUTPUT1-')],
          [sg.Text(' '), sg.Text(size=(80,1), key='-OUTPUT2-')],
          [sg.Button('Go'), sg.Button('Quit')]]

window = sg.Window('Bardoctorus\' Simple Image Resizer', layout)




while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    if event == 'Go':
        numSuccess = ir.doWork(values['-FOLDERPATH-'], values['-SIZE-'],True)
        print(numSuccess)
        fold = "Folder path: "
        size = "New Size: "
        fold += values['-FOLDERPATH-']
        size += values['-SIZE-']
        window['-OUTPUT1-'].update(fold)
        window['-OUTPUT2-'].update(size)
window.close()