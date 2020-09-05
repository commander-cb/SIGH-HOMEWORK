#export DISPLAY=10.67.107.137:0
#export PULSE_SERVER=tcp:10.67.107.137:4713
#xfwm4 & firefox
# hello_psg.py

import PySimpleGUI as sg

layout = [[sg.Text("you could try putting a bunch of code here see what Hello from PySimpleGUI\n"
"test - working newline character add . so i can keep going\n"
"and keep going\n\n""so this ends week one, make this fix it later")],
 [sg.Button("OK")], [sg.Button("no_ok"), sg.Button("no_1"), sg.Button("no_2"), sg.Button("no_3"), sg.Button("no_4")], [sg.Slider(), sg.Slider(), sg.Slider(), sg.Slider(),
  sg.Slider()], [sg.Button("SUBMIT")]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
        
        
    if event =="no_ok" or event == sg.WIN_CLOSED:
            break    
window.close()