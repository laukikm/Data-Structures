#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:04:01 2019

@author: Laukik Mujumdar
"""
import random

from build_heap import heap_insert_sift_up as heap_insert_sift_up
from build_heap import build_heap as build_heap


def check_if_min_heap(data):
    n=len(data)
    for i in range(n):
        #Compare parent with both of its children
        child_1=2*i+1
        child_2=1+child_1
        
        if(child_1>=n):
            return True
        elif(child_1==n-1):
            if(data[i]<=data[child_1]):
                return True
            else:
                return False
        else:
            #The current node has two children
            if(data[i]>data[child_1] or data[i]>data[child_2] ):
                return False
        
if __name__=='__main__':
    data_size=21;
    min_int=1
    max_int=21
    
    data=[]
    for i in range(data_size):
        data.append(0)
    
    is_discrepancy=0
    while(not is_discrepancy):
        #generate data pile
        for i in range(data_size):
            data[i]=random.randint(min_int,max_int)
        
        [heap,swaps]=build_heap(data)
        
        is_discrepancy=(not check_if_min_heap(heap)) and (len(swaps)<=4*data_size)
        

