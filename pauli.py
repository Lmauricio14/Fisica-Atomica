# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:24:29 2023

@author: jorgi
"""

import numpy as np
import sympy as sp

sx=sp.Matrix([[0,1],
              [1,0]])
sy=sp.Matrix([[0, -sp.I],
              [sp.I, 0]])
sz=sp.Matrix([[1,0],
              [0,-1]])

up=sp.Matrix([1,0])
down=sp.Matrix([0,1])

so=input(r'Ingresa la matriz que se va a evaluar (matriz en el exponente e^{iS/\hbar}): ')
s=input('Para un spin up o down: ')

if s=='up':
    spin=up
elif s=='down':
    spin=down
else:
    print ('Estado no válido')

if so=='sx':
    vec=sx*spin
elif so=='sy':
    vec=sy*spin
elif so=='sz':
    vec=sz*spin
else:
    print ('Matriz no válida')
    
c=sp.Matrix([np.cos(1/2),0])
d=sp.I*np.sin(1/2)*vec

final=c+d

print (final)