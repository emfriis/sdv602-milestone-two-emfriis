import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg

def login(event, values, state):
    '''
    This button opens a new window with the des gui.
    '''
    from layout.des_layout import des_layout
    cont = True
    if event == 'Log In':
        des_layout_view = des_layout()
        des_layout_view.self_layout()
        des_layout_view.render()
        des_layout_view.listen()
    return cont