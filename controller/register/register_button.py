import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg

def register(event, values, state):
    cont = True
    if event == 'Register':
        cont = True
    return cont