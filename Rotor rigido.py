from math import *
import numpy as np
import matplotlib.pyplot as plt

print('')
print('----------------------------------------------------------------------------')
print('')
print('Este programa nos ayuda a obtener tanto los valores de la energía rotacional,')
print('y a su vez nos grafica las funciones de onda para distintos valores de m.')
print('')
print('---------------------------------------------------------------------------')

print('')
m = int(input('Ingresa el valor máximo de m: '))
print('')
I= float(input('Ingresa el valor de I (en notación cientifica): '))
print('')

def e_r(m,I):
    hbar= 1.05457182*10**(-34)
    return (m**2*hbar**2)/(2*I)
print('El valor de la energía rotacional es:')
print('')
print(e_r(m,I))
print('')
print('La grafica de las funciones de onda es:')


f_r= lambda m,phi:sqrt(1/2)*np.cos(m*phi) #parte real 
f_i= lambda m,phi:sqrt(1/2)*np.sin(m*phi) #parte imaginaria   

for i in range(n):    
    x= np.arange(0,2*pi,0.01)
    y1= f_r(i,x)    
    y2= f_i(i,x)
    plt.plot(x,y1)
    plt.plot(x,y2)

plt.title("Funcion de onda para distintos valores de m")
plt.grid()
plt.show()