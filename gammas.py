from sympy import symbols, Matrix
from sympy.abc import x, y, z
import numpy as np
import matplotlib.pyplot as plt

# Definir los símbolos para las representaciones
NC, A1, A2, B1, B2, E = symbols('NC A₁ A₂ B₁ B₂ E')
RI = ['A₁','A₂','B₁','B₂','E']
N, Rx, Ry, Rz = symbols('N R1 R2 R3')

import pandas as pd

"""
Definir la tabla de caracteres (primer renglón es el no. de caracteres)
El último elemento del renglón indica x, y, z Rx, Ry o Rz
0=null, 1= x, y ó z, 2 = Rx, Ry ó Rz, 3 = xi o Ri
"""
# Definir los datos para cada tabla
tabla_c2v = {
    'NC': [1, 1, 1, 1, 0],
    'A₁': [1, 1, 1, 1, 1],
    'A₂': [1, 1, -1, -1, 2],
    'B₁': [1, -1, 1, -1, 3],
    'B₂': [1, -1, -1, 1, 3]
}

tabla_c3v = {
    'NC': [1, 2, 3, 0],
    'A₁': [1, 1, 1, 1],
    'A₂': [1, 1, -1, 2],
    'E': [2, -1, 0, 3]
}

tabla_c4v = {
    'NC': [1, 2, 1, 2, 2, 0],
    'A₁': [1, 1, 1, 1, 1, 1],
    'A₂': [1, 1, 1, -1, -1, 2],
    'B₁': [1, -1, 1, 1, -1, 0],
    'B₂': [1, -1, 1, -1, 1, 0],
    'E': [2, 0, -2, 0, 0, 3]
}

#funcion para subindices y superindices
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

# Convertir la tabla de caracteres en una matriz
c2v = np.array(list(tabla_c2v.values()))
c3v = np.array(list(tabla_c3v.values()))
c4v = np.array(list(tabla_c4v.values()))

# Coordenadas de los átomos en coordenadas esféricas
coor_H2O = np.array([[1, 0, 127.75], [1, 180, 127.75]])
coor_NH3 = np.array([[1,0,103 ],[1,120,103],[1,240,103]])
coor_NH4 = np.array([[1,0,103], [1,90,103], [1,180,103], [1,270,103]])
coor_XeOF4 = np.array([[1,0,90], [1,90,90], [1,180,90], [1,270,90], [1,0,0]])

def size(tabla_carac):
    #contamos numero de renglones de la tabla de caracteres seleccionada
    n = int(np.size(tabla_carac[0]))
    m = n
    return n,m
    
#obtenemos gamma traslacional (detectar q renglones deben sumarse)
def g_xyz(tc):
    n, m = size(tc)
    gamma_xyz = np.zeros(n-1,int)
    
    for i in range(1,n):
        if tc[i,-1]==1 or tc[i,-1]==3:
            gamma_xyz =  gamma_xyz + tc[i,0:-1]
    return gamma_xyz

#obtenemos gamma rotacional (detectar q renglones deben sumarse)
def g_rot(tc):
    n, m = size(tc)
    gamma_rot = np.zeros(n-1,int)
    for i in range(1,n):
        if tc[i,-1]==2 or tc[i,-1]==3:
            gamma_rot =  gamma_rot + tc[i,0:-1]
    return gamma_rot

def esfer_to_xyz(vec_pos):
    n_atoms = int(np.size(vec_pos)/3)
    vec_xyz = np.zeros((n_atoms,3))
    for i, vector in enumerate(vec_pos):
        vec_xyz[i,0] = round(vector[0]*np.sin(np.radians(vector[2]))*np.cos(np.radians(vector[1])),4)
        vec_xyz[i,1] = round(vector[0]*np.sin(np.radians(vector[2]))*np.sin(np.radians(vector[1])),4)
        vec_xyz[i,2] = round(vector[0]*np.cos(np.radians(vector[2])),4)
    return vec_xyz


def graficar_molecula(coor_esf, title='Molécula', ac_label='C', ar_label='H'):
    atom_central = np.array([0, 0, 0])  
    # Pásamos las coordenadas a cartesianas para graficar
    coordenadas = esfer_to_xyz(coor_esf)
    # Configurar la figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Dibujar átomos
    ax.scatter(*atom_central, s=50, c='lightgreen', marker='o')
    for i, h in enumerate(coordenadas):
        ax.scatter(*h, s=50, c='skyblue', marker='o')

    # Dibujar enlaces
    for h in coordenadas:
        ax.plot([atom_central[0], h[0]], [atom_central[1], h[1]], [atom_central[2], h[2]], c='b')

    # Etiquetas de los átomos
    ax.text(*atom_central, ac_label, fontsize=14, color='k', ha='left')
    for i, h in enumerate(coordenadas):
        ax.text(*h, ar_label+f'{i + 1}'.translate(SUB), fontsize=14, color='k', ha='left')

    # Configurar el aspecto del gráfico
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title(title)
    plt.show()
    
def cn(n,coor_esfe):
    n_atoms = int(np.size(coor_esfe)/3)
    coor_new = np.zeros((n_atoms,3))
    for i, atomo in enumerate(coor_esfe):
        coor_new[i,0] = atomo[0]
        coor_new[i,1] = atomo[1] + 360/n
        coor_new[i,2] = atomo[2]
    return coor_new

def sigma(plano,coor_esfer):
    n_atoms = int(np.size(coor_esfer)/3)
    coor_new = np.zeros((n_atoms,3))
    if plano=='v' or plano=='yz':
        for i, atomo in enumerate(coor_esfer):
            coor_new[i,0] = atomo[0]
            if atomo[1]<=180:
                coor_new[i,1] = 180 - atomo[1]
            elif atomo[1]>180:
                coor_new[i,1] = 540 - atomo[1]
            coor_new[i,2] = atomo[2]
    elif plano=='xz':
        for i, atomo in enumerate(coor_esfer):
            coor_new[i,0] = atomo[0]
            coor_new[i,1] = 360 - atomo[1]
            coor_new[i,2] = atomo[2]
    elif plano=='d':
        coor_new[0] = coor_esfer[3]
        coor_new[1] = coor_esfer[2]
        coor_new[2] = coor_esfer[1]
        coor_new[3] = coor_esfer[0]
    if n_atoms>4:
        coor_new[4] = coor_esfer[4]
    return coor_new 
    
#funcion para calcular el no. de veces que aparece c/ representación irreducible
def aRI(gamma, g_name, tc):
    n, m = size(tc) #dimensiones tabla caracteres
    orden = np.sum(tc[0]) #orden del grupo de simetria
    aRI = np.zeros(n-1,int)
    contador = 1
    for i in range(1,n):
        suma = 0
        for j in range(m-1):
            suma = suma + tc[i,j]*tc[0,j]*gamma[j]
        aRI[i-1] = suma/orden
        #creamos el string
        if aRI[i-1] != 0 and contador==1:
            string = str(aRI[i-1]) + RI[i-1] + " "
            contador = contador+1
        elif aRI[i-1] != 0:
            string = string + "+ " + str(aRI[i-1]) + RI[i-1] + " "
    print('\u0393_'+g_name+' = '+string)
    return aRI

#hacer función que obtenga el vector
def operaciones_simetria_c4v(molec_c4v, n, molec_name, ac, ar):
    #realizamos todas las operaciones de simetría en la molecula y graficamos
    xyz_c4v = esfer_to_xyz(molec_c4v)
    graficar_molecula(molec_c4v, title='Molécula '+molec_name, ac_label = ac, ar_label = ar)
    molec_c4v_c4 = cn(4,molec_c4v)
    graficar_molecula(molec_c4v_c4, title='Molécula '+molec_name+' C₄', ac_label = ac, ar_label = ar)
    molec_c4v_c2 = cn(2,molec_c4v)
    graficar_molecula(molec_c4v_c2, title='Molécula '+molec_name+' C₂', ac_label = ac, ar_label = ar)
    molec_c4v_sv = sigma('v',molec_c4v)
    graficar_molecula(molec_c4v_sv, title='Molécula '+molec_name+' σ_v', ac_label = ac, ar_label = ar)
    molec_c4v_sd = sigma('d',molec_c4v)
    graficar_molecula(molec_c4v_sd, title='Molécula '+molec_name+' σ_d', ac_label = ac, ar_label = ar)
    
    xyz_c4v_c4 = esfer_to_xyz(cn(4,molec_c4v))
    xyz_c4v_c2 = esfer_to_xyz(cn(2,molec_c4v))
    xyz_c4v_sv = esfer_to_xyz(sigma('v',molec_c4v))
    xyz_c4v_sd = esfer_to_xyz(sigma('d',molec_c4v))
    
    gamma_atoms = np.ones(5,int)
    gamma_atoms[0] = n
    for i in range(n-1):
        if all(xyz_c4v_c4[i] == xyz_c4v[i]):
            gamma_atoms[1] = gamma_atoms[1] + 1
    for i in range(n-1):
        if all(xyz_c4v_c2[i] == xyz_c4v[i]):
            gamma_atoms[2] = gamma_atoms[2] + 1
    for i in range(n-1):
        if all(xyz_c4v_sv[i] == xyz_c4v[i]):
            gamma_atoms[3] = gamma_atoms[3] + 1        
    for i in range(n-1):
        if all(xyz_c4v_sd[i] == xyz_c4v[i]):
            gamma_atoms[4] = gamma_atoms[4] + 1
    return gamma_atoms

def operaciones_simetria_c2v(molec_c2v, n, molec_name, ac, ar):
    #realizamos todas las operaciones de simetría en la molecula y graficamos
    xyz_c2v = esfer_to_xyz(molec_c2v)
    graficar_molecula(molec_c2v, title='Molécula '+molec_name, ac_label = ac, ar_label = ar)
    molec_c2v_c2 = cn(2,molec_c2v)
    graficar_molecula(molec_c2v_c2, title='Molécula '+molec_name+' C₂', ac_label = ac, ar_label = ar)
    molec_c2v_xz = sigma('xz',molec_c2v)
    graficar_molecula(molec_c2v_xz, title='Molécula '+molec_name+' σ_xz', ac_label = ac, ar_label = ar)
    molec_c2v_yz = sigma('yz',molec_c2v)
    graficar_molecula(molec_c2v_yz, title='Molécula '+molec_name+' σ_yz', ac_label = ac, ar_label = ar)
    
    xyz_c2v_c2 = esfer_to_xyz(molec_c2v_c2)
    xyz_c2v_sxz = esfer_to_xyz(molec_c2v_xz)
    xyz_c2v_syz = esfer_to_xyz(molec_c2v_yz)
    
    gamma_atoms = np.ones(4,int)
    gamma_atoms[0] = n
    for i in range(n-1):
        if all(xyz_c2v_c2[i] == xyz_c2v[i]):
            gamma_atoms[1] = gamma_atoms[1] + 1
    for i in range(n-1):
        if all(xyz_c2v_sxz[i] == xyz_c2v[i]):
            gamma_atoms[2] = gamma_atoms[2] + 1        
    for i in range(n-1):
        if all(xyz_c2v_syz[i] == xyz_c2v[i]):
            gamma_atoms[3] = gamma_atoms[3] + 1
    return gamma_atoms

#función que obtiene todas las gammas, representaciones irreducibles 
#y grafica las operaciones de simetria del grupo c4v
def c4v_main(molecule, n_atomos, molec_label,c,r):
    gamma_atom = operaciones_simetria_c4v(molecule, n_atomos, molec_label, ac=c, ar=r)
    g_xyz_c4v = g_xyz(c4v)
    print('\u0393_xyz   = ',g_xyz_c4v)
    print('\u0393_atom  = ',gamma_atom)
    #obtenemos gamma total
    g_total_c4v = g_xyz_c4v*gamma_atom
    print('\u0393_total = ',g_total_c4v,'\n')
    #obtenemos gamma rotacional
    g_rot_c4v = g_rot(c4v)
    print('\u0393_rot = ',g_rot_c4v,'\n')
    #obtenemos gamma vibracional
    print('\u0393_vib = \u0393_total - \u0393_xyz - \u0393_rot ')
    g_vib_c4v = g_total_c4v - g_xyz_c4v - g_rot_c4v
    print('\u0393_vib = ',g_vib_c4v,'\n')

    aRI_xyz = aRI(g_xyz_c4v,'xyz', c4v)
    aRI_rot = aRI(g_rot_c4v,'rot', c4v)
    aRI_vib = aRI(g_vib_c4v,'vib', c4v)
    
#función que obtiene todas las gammas, representaciones irreducibles 
#y grafica las operaciones de simetria del grupo c2v
def c2v_main(molecule, n_atomos, molec_label,c,r):
    gamma_atom = operaciones_simetria_c2v(molecule, n_atomos, molec_label, ac=c, ar=r)
    g_xyz_c2v = g_xyz(c2v)
    print('\u0393_xyz   = ',g_xyz_c2v)
    print('\u0393_atom  = ',gamma_atom)
    #obtenemos gamma total
    g_total_c2v = g_xyz_c2v*gamma_atom
    print('\u0393_total = ',g_total_c2v,'\n')
    #obtenemos gamma rotacional
    g_rot_c2v = g_rot(c2v)
    print('\u0393_rot = ',g_rot_c2v,'\n')
    #obtenemos gamma vibracional
    print('\u0393_vib = \u0393_total - \u0393_xyz - \u0393_rot ')
    g_vib_c2v = g_total_c2v - g_xyz_c2v - g_rot_c2v
    print('\u0393_vib = ',g_vib_c2v,'\n')

    aRI_xyz = aRI(g_xyz_c2v,'xyz', c2v)
    aRI_rot = aRI(g_rot_c2v,'rot', c2v)
    aRI_vib = aRI(g_vib_c2v,'vib', c2v)

c4v_main(coor_XeOF4, 6, "XeOF₄",'O','F')
c4v_main(coor_NH4, 5, "NH₄",'N','H')
c2v_main(coor_H2O, 3, 'H₂O','O','H')
