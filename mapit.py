# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 19:54:06 2020

@author: psvis
"""

import webbrowser
import sys
import pyperclip

sys.argv #['mapit.py', 'Eiffel', 'Tower']

if len(sys.argv)>1:
    #['mapit.py', 'Eiffel', 'Tower'] -> 'Eiffel Tower'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<address>
webbrowser.open('https://www.google.com/maps/place/' + address)