import PySimpleGUI as sg


# sg.theme('BluePurple')
#sg.theme_background_color('Yellow')

layout = [{sg.Text('Celsius:', font='Courier 15'), sg.Text(size=(15, 1), key='-OUTFAH-')},
          [sg.Input(key='-CEL-')],
          [sg.Button('Convert to F')],
          {sg.Text('Fahrenheit:', font='Courier 15'), sg.Text(size=(15, 1), key='-OUTCEL-')},
          [sg.Input(key='-FAH-')],
          [sg.Button('Convert to C')],
          [sg.Button('Exit')]]

window = sg.Window("Window's name", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Convert to F':
        cel = float(values['-CEL-'])
        window['-OUTFAH-'].update((cel * 9/5) + 32)

    if event == 'Convert to C':
        fah = float(values['-FAH-'])
        window['-OUTCEL-'].update((fah-32) * 5/9)


window.close()
