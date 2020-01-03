#!/usr/bin/python3

import sys, threading
import numpy as np
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

#import ipdb

def IsBinarySearchTree(tree,vertex,min_value,max_value):
    #Implement correct algorithm here
    if(len(tree)==0): return True
    [key,left_child,right_child]=tree[vertex]
  
    if(left_child==-1 and right_child==-1):
        if(key<max_value and key>min_value):
            return True
        else:
            return False
    elif(left_child==-1):
        if(key<min_value or key>max_value):
            return False
        else:
            return IsBinarySearchTree(tree,right_child,key,max_value)
    elif(right_child==-1):
        if(key<min_value or key>max_value):
            return False
        else:
            return IsBinarySearchTree(tree,left_child,min_value,key)
    else:
        return IsBinarySearchTree(tree,left_child,min_value,key) and IsBinarySearchTree(tree,right_child,key,max_value)

def main():
  nodes = int(input()) #int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, input().split()))) #sys.stdin.readline().strip().split()

  #ipdb.set_trace()
  if IsBinarySearchTree(tree,0,-np.inf,np.inf):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
