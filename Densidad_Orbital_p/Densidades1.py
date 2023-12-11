# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:16:48 2023

@author: jorgi
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

s_orbitals = pd.read_csv(r'C:\Users\jorgi\Documents\Densidad_Orbital_p\Orbitales.csv')

"""
Podemos imprimir los valores que van a tener los orbitales en función del radio
que se encuentra la partícula 
"""

s_orbitals.head(10)

fig, ax = plt.subplots()
ax.plot("r", "1s", data=s_orbitals)
ax.plot("r", "2s", data=s_orbitals)
ax.plot("r", "3s", data=s_orbitals)
ax.legend()

ax.set_ylabel(r"$\psi$")
ax.set_xlabel("r")
ax.set_xlim(-0.1, 14)

"""
Para cada orbital ahora trabajando con las 3 dimensiones
"""

orbital_px=pd.read_csv(r'C:\Users\jorgi\Documents\Densidad_Orbital_p\px_2D.csv', header=None)
orbital_py=pd.read_csv(r'C:\Users\jorgi\Documents\Densidad_Orbital_p\py_2D.csv', header=None)
orbital_pz=pd.read_csv(r'C:\Users\jorgi\Documents\Densidad_Orbital_p\pz_2D.csv', header=None)


px_values = orbital_px.iloc[1:, 1:]
py_values = orbital_py.iloc[1:, 1:]
pz_values = orbital_pz.iloc[1:, 1:]


mpl.rcParams['font.size'] = 14
mpl.rcParams['legend.fontsize'] = 'large'
mpl.rcParams['figure.titlesize'] = 'medium'

#Para plano xy
x = orbital_px.iloc[0, 1:]
y = orbital_px.iloc[1:, 0]
pmin = px_values.min().min()
pmax = px_values.max().max()
levels = np.linspace(pmin, pmax, 30)

fig, ax = plt.subplots()
ticks = np.linspace(pmin, pmax, 6)

CS = ax.contourf(x, y, px_values, cmap="RdBu", levels=levels)

fig.colorbar(CS)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Densidad del orbital P (z en plano xy)', fontsize=12)

#Para plano  yz
x = orbital_py.iloc[0, 1:]
y = orbital_py.iloc[1:, 0]
pmin = py_values.min().min()
pmax = py_values.max().max()
levels = np.linspace(pmin, pmax, 30)

fig, ax = plt.subplots()
ticks = np.linspace(pmin, pmax, 6)

CS = ax.contourf(x, y, py_values, cmap="RdBu", levels=levels)

fig.colorbar(CS)
ax.set_xlabel('y')
ax.set_ylabel('z')
ax.set_title('Densidad del orbital P (x en plano yz)', fontsize=12)

#Para plano xz
x = orbital_pz.iloc[0, 1:]
y = orbital_pz.iloc[1:, 0]
pmin = pz_values.min().min()
pmax = pz_values.max().max()
levels = np.linspace(pmin, pmax, 30)

fig, ax = plt.subplots()
ticks = np.linspace(pmin, pmax, 6)

CS = ax.contourf(x, y, pz_values, cmap="RdBu", levels=levels)

fig.colorbar(CS)
ax.set_xlabel('x')
ax.set_ylabel('z')
ax.set_title('Densidad del orbital P (y en plano xz)', fontsize=12)
