#! encoding: UTF-8
#! /usr/bin/python 

import math

Cero=0.00001

def f(x):
 return math.sin(x)

def biseccion(a,b,tol):
 c=float((a+b)/2.0)
 while f(c) != Cero and abs(b-a) > tol:
  if f(a) * f(c) < Cero:
   b = c;
  else:
   a = c;
  c = (a+b)/2.0
 return c

print 'Calcular la ra�z de sen de x'
a = float(raw_input('Valor a del intervalo: '))
b = float(raw_input('Valor b del intervalo: '))
t = 0.00000000000001
r = biseccion(a,b,t)
print "El valor de la ra�z de seno de x es: %f"%(r)