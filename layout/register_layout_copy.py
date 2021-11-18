import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
import controller.register.register_button as register_button
import controller.login.exit_button as exit_button

class register_layout_copy(object):
    
    def __init__(self):
        self.window = None
        self.layout = []
        self.components = {'components': False}
        self.controls = []
        
    def self_layout(self, **kwargs):
        sg.theme('Dark Blue 3')
        
        self.components['register_button'] = sg.Button(button_text = 'Register')
        self.controls += [register_button.register]
        
        self.controls += [exit_button.exit]
        
        self.layout = [
            [sg.Text('Email')],
            [sg.Input()],
            [sg.Text('Username')],
            [sg.Input()],
            [sg.Text('Password')],
            [sg.Input()],
            [self.components['register_button']]
        ]
        
    def render(self):
        if self.layout != []:
            self.window = sg.Window('Register', self.layout, grab_anywhere=False, finalize=True)
            
    def listen(self):
        if self.window != None:
            cont = True
            while cont == True:
                event, values = self.window.read()
                for control in self.controls:
                    cont = control(event, values, {'view':self})
            self.window.close()