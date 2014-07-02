#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 1, 2014

@author: anroco

how to determine the number of times an item is repeated in a list in python?

¿como hacer para determinar la cantidad de veces que se repite un item en una
lista python?
'''

#create a list
lista = list('hello world')
print (lista)

#return the number of times it appears in the list.
count = lista.count('l')
print (count)

count = lista.count('o')
print (count)

count = lista.count('m')
print (count)
