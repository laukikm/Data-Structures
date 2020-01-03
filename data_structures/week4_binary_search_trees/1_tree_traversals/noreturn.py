#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 17:53:25 2019

@author: laukik
"""

# python3
#Solution by Laukik Mujumdar
import sys, threading

sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(input()) #int(input())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    self.result=[]
    for i in range(self.n):
      [a, b, c] = map(int,input().split()) #map(int, input().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self,vertex):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    #ipdb.set_trace()
    if(self.left[vertex]==-1 and self.right[vertex]==-1):
        self.result.extend([self.key[vertex]])
    elif(self.left[vertex]==-1):
        
        self.result.extend([self.key[vertex]])
        self.inOrder(self.right[vertex]) #O(k), k is the size of the result
        
    elif self.right[vertex]==-1:
        
        self.inOrder(self.left[vertex]) #O(k), k is the size of the result
        self.result.extend([self.key[vertex]]) #O(1))
        
    
    else:
        self.inOrder(self.left[vertex])
        self.result.extend([self.key[vertex]])
        self.inOrder(self.right[vertex]) #O(n)
        #return self.result
                
    #return self.result

  def preOrder(self,vertex):
    # Finish the implementation
    # You may need to add a new recursive method to do that

    if(self.left[vertex]==-1 and self.right[vertex]==-1):
        self.result.extend([self.key[vertex]])
    elif(self.left[vertex]==-1):
        
        self.result.extend([self.key[vertex]])
        self.preOrder(self.right[vertex]) #O(k), k is the size of the result 
        
        
    elif self.right[vertex]==-1:
        self.result.extend([self.key[vertex]])
        self.preOrder(self.left[vertex]) #O(k), k is the size of the result 
        
  
    else:
        self.result.extend([self.key[vertex]])
        self.preOrder(self.left[vertex])
        self.preOrder(self.right[vertex])
        #temp.extend([self.key[vertex]]) #O(1) 
        #temp.extend(self.preOrder(self.left[vertex])) #O(k), k is the size of the result
        #temp.extend(self.preOrder(self.right[vertex])) #O(n-k), k is the size of left sub tree elem count
        
  
  

  def postOrder(self,vertex):
    
    
    # Finish the implementation
    # You may need to add a new recursive method to do that

    if(self.left[vertex]==-1 and self.right[vertex]==-1):
        self.result.extend([self.key[vertex]]) #O(1)
    elif(self.left[vertex]==-1):
        
        
        self.postOrder(self.right[vertex])
        self.result.extend([self.key[vertex]])
        #result.extend([self.key[vertex]]) #O(1)
        
    elif self.right[vertex]==-1:
        
        self.postOrder(self.left[vertex])
        self.result.extend([self.key[vertex]]) #O(k), k is the size of the result
        #self.result.extend([self.key[vertex]]) #O(1)
        #return self.result
  
    else:
        
        self.postOrder(self.left[vertex])
        self.postOrder(self.right[vertex])
        self.result.extend([self.key[vertex]])
        #temp.extend(self.postOrder(self.left[vertex])) #O(k), k is the size of the result
        #temp.extend(self.postOrder(self.right[vertex])) #O(n-k), k is the size of left sub tree elem count
        #temp.extend([self.key[vertex]]) #O(1)
        #return self.result
    

def main():
    tree = TreeOrders()
    tree.read()
    tree.inOrder(0)
    print(" ".join(str(x) for x in tree.result))
    tree.result=[]
    tree.preOrder(0)
    print(" ".join(str(x) for x in tree.result))
    tree.result=[]
    tree.postOrder(0)
    print(" ".join(str(x) for x in tree.result))
threading.Thread(target=main).start()

