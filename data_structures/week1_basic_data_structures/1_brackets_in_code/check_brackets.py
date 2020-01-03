# python3
#Solution by Laukik Mujumdar

from collections import namedtuple

#import ipdb

Bracket = namedtuple("Bracket", ["char", "position"])




def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    position=0
    for i, next in enumerate(text):
        #print('next=',next)
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)   
            #print(opening_brackets_stack)
            position=i+1
            pass
        
        #ipdb.set_trace()
        
        if next in ")]}":
            # Process closing bracket, write your code here
            #print(opening_brackets_stack)
            if(len(opening_brackets_stack)==0):
                return i+1 #Mismatch exists
                
                
            elif(not are_matching(opening_brackets_stack.pop(),next)):
                return i+1
            position-=1
            pass
        
    if(len(opening_brackets_stack)==0):
        return 'No_Mismatch'
    else:
        return position
        


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if(not mismatch=='No_Mismatch'):
        print(mismatch)
    else:
        print('Success')

if __name__ == "__main__":
    main()
