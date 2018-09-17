# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 11:12:22 2018

@author: Bill
"""

print('\tdecimal\tbinary\thex')
go = -1
while go < 31:
    go = go + 1
    print('\t' + str(go) + '\t' + bin(go) + '\t' + hex(go))
    
#print(bin(0))
#   hex()