#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:38:46 2023

@author: lagarto
"""

import numpy as np
import pandas as pd

print("Este programa obtiene el grupo puntual de simetría de una partícula")

def perreo():
    
    
    a = int(input("¿La molécula es lineal? (0 = no, 1 = sí): "))
    
    
    if a == 0:
        
        print("La molécula no es lineal")
        
####### MOLÉCULA NO LINEAL ###
        
        b = int(input("La molecula tiene dos o mas Cn con n > 2 (0 = no, 1 = sí):"))
        
####### Molecula sin CN con n > 2 ###
        if b == 0:
            
            c = int(input("La partícula tiene Cn? (0 = no, 1 = sí):"))
            
            if c == 0:
                
                d = int(input("La partícula tiene \u03C3 n? (0 = no, 1 = sí):"))
                
                if d == 0:
                    
                    xyz = int(input("¿La molécula tiene centro de inversión? (0 = no, 1 = sí): "))
                    
                    if xyz ==0:
                        print("El grupo puntual de la partícula es C1")
                        
                        
                    elif xyz ==1:
                        
                        print("El grupo puntual de la partícula es Ci")
                        
                    else: 
                        print("Entrada incorrecta, vuelva a empezar")    
                        
                if d == 1:
                    print("El grupo puntual de la partícula es Cs")
                    
            if c == 1:
                
                abc = int(input("El Cn tiene nC2 perpendicular a Cn? (0 = no, 1 = sí):"))
                
                if abc == 0:
                    
                    sh = int(input("La partícula tiene \u03C3 h? (0 = no, 1 = sí):"))
                    
                    if sh == 0:
                        
                        nu = int(input("La partícula tiene n \u03C3 v? (0 = no, 1 = sí):"))
                        
                        if nu == 0:
                    
                            
                            Ss = int(input("La partícula tiene S2n? (0 = no, 1 = sí):"))
                            
                            if Ss == 0:
                                
                                print("El grupo puntual es S2n")
                            
                            elif Ss == 1:
                                
                                print("El grupo puntual es Cn")
########################### ENTRADA INCORRECTA ###   
                         
                            else: 
                                print("Entrada incorrecta, vuelva a empezar")
                            
                        elif nu == 1:
                            
                            print("El grupo puntual de la partócula es Cnv")
                            
######################## ENTRADA INCORRECTA ###                
    
                        else: 
                            print("Entrada incorrecta, vuelva a empezar")    
                    
                    elif sh == 1:
                        
                        print("El grupo puntual de la partícula es Cnh")
                        
#################### ENTRADA INCORRECTA ###             
                    else: 
                       
                        print("Entrada incorrecta, vuelva a empezar")
                        
                if abc == 1:
                        
                    sih =  int(input("La partícula tiene \u03C3 h? (0 = no, 1 = sí):"))

                    if sih == 0:
                        
                        nsv =  int(input("La partícula tiene n \u03C3 v? (0 = no, 1 = sí):"))
                        
                        if nsv == 0:
                            
                            print("El grupo puntual de la partícula es Dn")
                            
                        elif nsv ==1:
                            
                            print("El grupo puntual de la partícula es Dnd")
####################### ENTRADA INCORRECTA ###                        
                        else: 
                            print("Entrada incorrecta, vuelva a empezar")
                        
                    elif sih == 1:
                        
                        print("El grupo puntual es Dnh")
################### ENTRADA INCORRECTA ###
                    else: 
                        
                        print("Entrada incorrecta, vuelva a empezar")
                        

####### Molecula sin CN con n > 2 ###
        elif b ==1:
        
            invs = int(input("La partícula tiene centro de inversión? (0 = no, 1 = sí):"))
            
            if invs == 0:
                
                print("El grupo puntual de la partícula es Td")
                
            elif invs == 1:
                
                cin = int(input("La partícula tiene C5? (0 = no, 1 = sí):"))
                
                if cin == 0:
                    
                    print("El grupo puntual de la partícula es Oh")
                    
                elif cin == 1:
                    
                    print("El grupo puntual de la partócula es Ih")

############### ENTRADA INCORRECTA ###
                else:
                    
                    print("Entrada incorrecta, vuelva a empezar")
                    
########### ENTRADA INCORRECTA ###          
            else:
                
                print("Entrada incorrecta, vuelva a empezar")
        
            
####### ENTRADA INCORRECTA ###
        else: 
            
            print("Entrada incorrecta, vuelva a empezar")
    
        
        
        
    elif a== 1:
        
        
        print("La partícula es lineal, procedemos la siguiente paso")
        ###PASOS PARA LA MOLECULA LINEAL###
        lin = int(input("¿La molécula tiene centro de inversión? (0 = no, 1 = sí): "))
        
        
        if lin ==0:
            print("El grupo puntual de la partícula es D\u221Eh")
        
        
        elif lin ==1:
            print("El grupo puntual de la partícula es C\u221Ev")
        
        
        else: 
            print("Entrada incorrecta, vuelva a empezar")
        
        
        ###PASOS PARA LA MOLECULA LINEAL###
        
        
        
        
        
        
        
        #### ENTRADA INCORRECTA ###
    else:
        print("Entrada incorrecta, vuelva a empezar: ")
    return

perreo()
    