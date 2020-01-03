#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 17:09:07 2019

@author: laukik
"""
#Creates a random binary tree and tests traversal methods

import random as rd
import sys, threading
import ipdb

sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self,n):
    self.n = n
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    self.result=[]
    for i in range(self.n):
        if(i<self.n/2-1):
            [a, b, c] = [rd.randint(0,self.n),2*i+1,2*i+2]
        else:
            #print(i)
            [a, b, c] = [rd.randint(0,self.n),-1,-1]
        #print(b,c)
        self.key[i] = a
        self.left[i] = b
        self.right[i] = c

  def inOrder(self,vertex):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    result=[]
    #ipdb.set_trace()
    if(self.left[vertex]==-1 and self.right[vertex]==-1):
        return [self.key[vertex]] #O(1)
    elif(self.left[vertex]==-1):
        result=[]
        result.extend([self.key[vertex]]) #O(1)
        result.extend(self.inOrder(self.right[vertex])) #O(k), k is the size of the result
        return result
    elif self.right[vertex]==-1:
        result=[]
        result.extend(self.inOrder(self.left[vertex])) #O(k), k is the size of the result
        result.extend([self.key[vertex]]) #O(1)
        return result
    
    else:
        temp=[]
        temp.extend(self.inOrder(self.left[vertex])) #O(k), k is the size of the result
        temp.extend([self.key[vertex]]) #O(1)
        temp.extend(self.inOrder(self.right[vertex])) #O(n-k), k is the left sub tree element count
        return temp
                
    #return self.result

  def preOrder(self,vertex):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that

    if(self.left[vertex]==-1 and self.right[vertex]==-1):
        return [self.key[vertex]]
    elif(self.left[vertex]==-1):
        result=[]
        result.extend([self.key[vertex]]) #O(1)
        result.extend(self.preOrder(self.right[vertex])) #O(k), k is the size of the result
        return result
    elif self.right[vertex]==-1:
        result=[]
        result.extend([self.key[vertex]]) #O(1)
        result.extend(self.preOrder(self.left[vertex])) #O(k), k is the size of the result
        return result
  
    else:
        temp=[]
        temp.extend([self.key[vertex]]) #O(1) 
        temp.extend(self.preOrder(self.left[vertex])) #O(k), k is the size of the result
        temp.extend(self.preOrder(self.right[vertex])) #O(n-k), k is the size of left sub tree elem count
        return temp
  
  

  def postOrder(self,vertex):
    
    
    # Finish the implementation
    # You may need to add a new recursive method to do that

    if(self.left[vertex]==-1 and self.right[vertex]==-1):
        return [self.key[vertex]] #O(1)
    elif(self.left[vertex]==-1):
        result=[]
        
        result.extend(self.postOrder(self.right[vertex])) #O(k), k is the size of the result
        result.extend([self.key[vertex]]) #O(1)
        return result
    elif self.right[vertex]==-1:
        
        result=[]
        result.extend(self.postOrder(self.left[vertex])) #O(k), k is the size of the result
        result.extend([self.key[vertex]]) #O(1)
        return result
  
    else:
        temp=[]
        
        temp.extend(self.postOrder(self.left[vertex])) #O(k), k is the size of the result
        temp.extend(self.postOrder(self.right[vertex])) #O(n-k), k is the size of left sub tree elem count
        temp.extend([self.key[vertex]]) #O(1)
        return temp
    
if __name__=='__main__':
    n=10**2 #int(input())
    while(True):
        tree=TreeOrders()
        tree.read(n)
        rord=tree.inOrder(0)
        pord=tree.postOrder(0)
        prord=tree.preOrder(0)
        
