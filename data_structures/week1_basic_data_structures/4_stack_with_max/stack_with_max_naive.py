#python3
import sys

#import ipdb

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max=[] 
    def Push(self, a):
        self.__stack.append(a)
        if(len(self.max)==0):
            maximum_element=0
        else:
            maximum_element=self.max[len(self.max)-1]
        if(a>=maximum_element):
            self.max.append(a)
    def Pop(self):
        assert(len(self.__stack))
        last_element=self.__stack[len(self.__stack)-1]
        if(len(self.max)==0):
            maximum_element=0
        else:
            maximum_element=self.max[len(self.max)-1]
        
        if(last_element==maximum_element):
            self.max.pop()
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        if(len(self.max)==0):
            maximum_element=0
        else:
            maximum_element=self.max[len(self.max)-1]
        return maximum_element


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        
        
        query = sys.stdin.readline().split()
        
        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
        
        
        """
        #ipdb.set_trace()
        query=input()
        
        if int(query[0]) == 1:
            stack.Push(int(query[1]))
        elif int(query[0]) == 0:
            stack.Pop()
        elif int(query[0]) == 2:
            print(stack.Max())
        else:
            assert(0)
        """