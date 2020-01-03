# python3
#Solution by Laukik Mujumdar

import math
#import ipdb


def sift_down(data,parent_index,swaps):
    n=len(data)
    
    child_1=parent_index*2+1
    child_2=1+child_1
    #ipdb.set_trace()
    if(child_1>=n):
        pass
    
    elif(child_1==n-1):
        if(data[child_1]<data[parent_index]):
            temp=data[parent_index]
            data[parent_index]=data[child_1]
            data[child_1]=temp
            
            swaps.append((parent_index,child_1))
    else:
        parent=data[parent_index]
        c1=data[child_1]
        c2=data[child_2]
        
        if(parent>c1 and c1<=c2):
            data[parent_index]=c1
            data[child_1]=parent
            swaps.append((parent_index,child_1))
            sift_down(data,child_1,swaps)
        elif(parent>c2 and c2<=c1):
            data[parent_index]=c2
            data[child_2]=parent
            swaps.append((parent_index,child_2))
            sift_down(data,child_2,swaps)
            
            


def heap_insert_sift_up(heap,elem):
    #Assume that the heap is in place and only one element is to be inserted
    
    #Append the element to the bottom of the tree and sift it up
    #Sifting up=O(log(n)); Summation from 1 to n of O(log(n))=O(n*log(n)). (This doesn't work. Why?)
    #ipdb.set_trace()
    heap.append(elem)
    
    child_index=len(heap)-1
    
    abort_signal=False
    n_swaps=0
    
    swaps=[]
 
    #ipdb.set_trace
    while(not abort_signal and child_index!=0):
        parent_index=math.ceil(child_index/2)-1
        if(heap[child_index]<heap[parent_index]):
            #print('heap=',heap)
            temp=heap[child_index]
            heap[child_index]=heap[parent_index]
            heap[parent_index]=temp
            
            n_swaps+=1
            swaps.append((parent_index,child_index))
            child_index=parent_index
        else:
            abort_signal=True
            
    return swaps
    #As python uses pass by reference, the heap doesn't need to be returned    
        

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    
    '''
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    '''
    
    '''
    #My implementation below, using SiftUp
    heap=[]
    #ipdb.set_trace()
    for i in range(len(data)):
        swaps.extend(heap_insert_sift_up(heap,data[i]))
    '''
    n=len(data)
    last_parent=math.ceil(n/2)-1
    for i in range(last_parent+1):
        sift_down(data,last_parent-i,swaps)
    
    #ipdb.set_trace()
    return data,swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    
    [heap,swaps] = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    #print(heap)

if __name__ == "__main__":
    main()
