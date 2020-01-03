#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 22:52:21 2019

@author: laukik
"""

from is_bst import IsBinarySearchTree as isb
import random as rd
import numpy as np

def isb_naive(tree):
    #Hardcoded for a tree of size 7
    n=7
    
    if(not(tree[3][0]<tree[1][0] and tree[4][0]>tree[1][0])):
        return False
    
    if(not(tree[5][0]<tree[2][0] and tree[6][0]>tree[2][0])):
        return False
    if(tree[4][0]>tree[0][0] or tree[5][0]<tree[0][0]):
        return False
    return True
    
if __name__=='__main__':
    #Program a random binary tree generator
    n=7
    a1=False
    a2=False
    while(a1==a2):
        for i in range(n):
            t1=[]
            t2=[]
            key=rd.randint(0,100)
            key2=rd.randint(0,100)
            if(i<3):
                lc=2*i+1
                rc=2*i+2
            else:
                    lc=-1
                    rc=-1
            t1.append([key,lc,rc])
            
        a1=isb(tree,0,-np.inf,np.inf)
        a2=isb_naive(tree)
        
        if(a1!=a2):
            print(tree)
        #t2.append([key2,lc,rc])