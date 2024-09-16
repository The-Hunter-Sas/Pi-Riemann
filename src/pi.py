#!/usr/bin/env python

def funcion(x):
    return 4/(1+(x*x)) #función a integrar

def riemann(n,a,b): #función acumuladora
    acumulador = 0.0
    cantidad = n
    ancho = (b-a)/n #el limite superior menos el inferior entre la cantidad de particiones

    for i in range(cantidad):

        acumulador += función((i/n) + ancho/2) #se evalúa en la función cada entrada del for entre el numero de particiones mas la mitad del ancho

    return acumulador * ancho

a=0
b=1
n=1000
resultado = riemann(n,a,b)
print(resultado)
