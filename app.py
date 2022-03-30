from re import MULTILINE
from tkinter.constants import CENTER, LEFT
import PySimpleGUI as sg
import secrets
import string
import io
import qrcode

# Theme apply
sg.theme('DarkGrey9')

# Define the window's contents
layout = [[sg.Text("How many characters do you want for your password: "),sg.Input(size=(20,1),key='-INPUT-',justification=CENTER)],
          [sg.Text(key='-OUTPUT-')],
          [sg.InputText(key='-OUTPUT1-', size=(67,1), use_readonly_for_disable=True, disabled=True, text_color=sg.theme_element_text_color())],
          [sg.Stretch(),sg.Text(key='-OUTPUT2-', justification=CENTER, font='Courier'),sg.Stretch()],
          [sg.Button('Generate'), sg.Button('Quit')]]

# Create the window
window = sg.Window('P@ssw0rd G3n3r@t0r', layout, finalize=True)

window['-OUTPUT1-'].Widget.config(readonlybackground=sg.theme_background_color())
window['-OUTPUT1-'].Widget.config(borderwidth=0)

# Processing
def password_generator(pass_len):
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for i in range(pass_len))
    return password

def qrcode_generator(string):
    qr = qrcode.QRCode()
    qr.add_data(string)
    f = io.StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    qr_code = f.read()
    print(qr_code)
    img = qrcode.make(string)
    type(img)  # qrcode.image.pil.PilImage
    img.save("QR.png")
    return qr_code

def info(n):
    list = [
    'Terrible! Crackable in 2 minutes. Too short!',
    'Terrible! Crackable in 2 minutes. Too short!',
    'Terrible! Crackable in 2 minutes. Too short!',
    'Terrible! Crackable in 2 minutes. Too short!',
    'Terrible! Crackable in 2 minutes. Too short!',
    'Terrible! Crackable in 2 minutes. Too short!',
    'Terrible! Crackable in 2 minutes. Too short!',
    'Terrible! Crackable in 17 minutes. Too short!',
    'Weak! Crackable in 3 hours. Too short!',
    'Weak! Crackable in 1 day. Too short!',
    'Weak! Crackable in 12 days. Too short!',
    'Good! Could take 4 months to crack. But consider adding length!',
    'Good! Could take 3 years to crack. But consider adding length!',
    'Good! Could take 32 years to crack. But consider adding length!',
    'Good! Could take 317 years to crack. But consider adding length!',
    'Good! Could take 3,171 years to crack. But consider adding length!',
    'Good! Could take 31,710 years to crack. But consider adding length!',
    'Strong! Could take 317,098 years to crack.',
    'Strong! Could take 3 million years to crack.',
    'Strong! Could take 32 million years to crack.',
    'Strong! Could take 317 million years to crack.',
    'Strong! Could take 3 billion years to crack.',
    'Strong! Could take 32 billion years to crack.',
    'Strong! Could take 317 billion years to crack.',
    'Strong! Could take 3,169 billion years to crack.',
    'Strong! Could take 31,689 billion years to crack.',
    'Strong! Could take 316,888 billion years to crack.',
    'Strong! Could take 3,168,876 billion years to crack.',
    'Strong! Could take 31,688,765 billion years to crack.',
    'Strong! Could take 316,887,646 billion years to crack.',
    'Strong! Could take 3,168,876,462 billion years to crack.',
    'Strong! Could take 31,688,764,615 billion years to crack.',
    'Strong! Could take 316,887,646,154 billion years to crack.',
    'Strong! Could take 3,168,876,461,541 billion years to crack.',
    'Strong! Could take 31,688,764,615,413 billion years to crack.',
    'Strong! Could take 316,887,646,154,128 billion years to crack.',
    'Strong! Could take 3,168,876,461,541,279 billion years to crack.',
    'Strong! Could take 31,688,764,615,412,790 billion years to crack.',
    'Strong! Could take 316,887,646,154,127,940 billion years to crack.',
    'Strong! Could take 3,168,876,461,541,280,000 billion years to crack.',
    'Strong! Could take 31,688,764,615,412,793,000 billion years to crack.',
    'Strong! Could take 316,887,646,154,127,900,000 billion years to crack.',
    'Strong! Could take 3,168,876,461,541,279,400,000 billion years to crack.',
    'Strong! Could take 31,688,764,615,412,794,000,000 billion years to crack.',
    'Strong! Could take 316,887,646,154,127,960,000,000 billion years to crack.',
    'Strong! Could take 2,566,789,933,848,436,300,000,000 billion years to crack.',
    'Strong! Could take 31,688,764,615,412,797,000,000,000 billion years to crack.',
    'Strong! Could take 316,887,646,154,127,950,000,000,000 billion years to crack.',
    'Strong! Could take 3,168,876,461,541,280,000,000,000,000 billion years to crack.',
    'Strong! Could take 31,688,764,615,412,800,000,000,000,000 billion years to crack.',
    'Strong! Could take 316,887,646,154,127,970,000,000,000,000 billion years to crack.'
    ]
    info = '\n' + list[n]
    return info

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.Read()
    
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    user_input = values['-INPUT-']
    if True:
        try:
            val = int(user_input)
            if user_input =="":
                window['-OUTPUT-'].update('You must enter at least a number')
                window['-OUTPUT1-'].update('Please, re-enter! and then Click "Ok"')
                window['-OUTPUT2-'].update('')
            elif int(user_input) == 0:
                window['-OUTPUT-'].update('Minimum value must not be Zero')
                window['-OUTPUT1-'].update('Please, re-enter! and then Click "Ok"')
                window['-OUTPUT2-'].update('')
            elif int(user_input) > 50:
                window['-OUTPUT-'].update('You crossed the limit of resourse')
                window['-OUTPUT1-'].update('Please, re-enter! and then Click "Ok"')
                window['-OUTPUT2-'].update('')
            else:
                user_input_updated = user_input
                # info(int(user_input_updated))
                window['-OUTPUT-'].update('Well done, password length is: ' + user_input_updated + info(int(user_input_updated)))
                password = password_generator(int(user_input_updated))
                qr = qrcode_generator(password)
                text = 'Here it is: ' + password
                window['-OUTPUT1-'].update(text)
                window['-OUTPUT2-'].update(qr)                                  
        except ValueError: 
            window['-OUTPUT-'].update('Your input must be a number')
            window['-OUTPUT1-'].update('Please, re-enter! and then Click "Ok"')
            window['-OUTPUT2-'].update('')

# Finish up by removing from the screen
window.close()