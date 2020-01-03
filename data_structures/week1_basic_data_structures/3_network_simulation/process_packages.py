# python3
#Solution by Laukik Mujumdar

import ipdb

from collections import namedtuple
from collections import deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = 0
        self.buffer_queue=deque() #This is the buffer queue

    def process(self, request):
        
        # write your code here
        #print('buffer=',self.buffer_queue)
        #print('request=',request)
        response=Response
        
        #Get rid of the elements that should've been gone by now
        
        current_time=request.arrived_at
        t=self.finish_time
        
        #replica_buffer=list(self.buffer_queue) #O(1) since the buffer size is constant
        #If this is not done, changing buffer_queue also changes the replica_buffer
        
        #ipdb.set_trace()
        iterator=0
        while(iterator<len(self.buffer_queue)):#for iterator in len(self.buffer_queue):
            i=self.buffer_queue[iterator]
            if(t<i.arrived_at):
                t=i.arrived_at+i.time_to_process
            else:
                t+=i.time_to_process
            
            if(t<=current_time):#Remove element 
                self.buffer_queue.popleft() #O(1) as the buffer size is constant
                self.finish_time=t
                iterator-=1
            iterator+=1
            
        #If there's no space in the buffer, output -1
        if(len(self.buffer_queue)==self.size):
            response.was_dropped=True
        else:
            #Add request to the buffer
            t=self.finish_time #The time by when previous requests will be dealt with
            for i in self.buffer_queue: #O(1) since the buffer size is constant
                if(t<i.arrived_at):
                    t=i.arrived_at+i.time_to_process
                else:
                    t+=i.time_to_process
                    
            
            self.buffer_queue.append(request) #O(1)
            response.was_dropped=False
            if(t<request.arrived_at):
                response.started_at=request.arrived_at
            else:
                response.started_at=t
                
            
       
        return response


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        #responses.append(buffer.process(request))
        response=buffer.process(request) #O(1)
        print(response.started_at if not response.was_dropped else -1)
        #print('request=',request.arrived_at)
        #print('response=',buffer.process(request).started_at)
    return True


def main():
    a=1
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    
    responses = process_requests(requests, buffer)

    #for response in responses:
        #ipdb.set_trace()
        #print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
