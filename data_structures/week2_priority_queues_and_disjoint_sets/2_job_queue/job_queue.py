# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

import heapq as hq

#import ipdb

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    
    next_free_time = [0] * n_workers
    for job in jobs: #O(m)
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w]) #O(n)
        result.append(AssignedJob(next_worker, next_free_time[next_worker])) #O(1)
        next_free_time[next_worker] += job

    return result
    

def assign_jobs_heapq(n_workers,jobs):
    result=[]
    
    #This array represents if the given thread is free or not
    free_or_not=[0]*n_workers
    starting_times=[0]*n_workers #This represents when each thread started their jobs
    
    next_free_times=[0]*n_workers
    
    free_times_heap=[]
    for i in range(n_workers):
        free_times_heap.append([next_free_times[i],i]) #This is already stored as a heap. 1st element is the priority, the second element is the index
    
    #ipdb.set_trace()
    min_next_free_time=0
    
    workers_heap=list(range(n_workers)) #This is the list of free workers, stored as a heap
    
    current_time=0
    for job in jobs: #O(m)
        
        '''
        if(len(workers_heap)==0): #If all workers are busy
            for i in range(n_workers): #O(n)
                if(next_free_times[i]<=min_next_free_time):
                    hq.heappush(workers_heap,i) #O(log(n))
            
            current_time=min_next_free_time
        next_worker=hq.heappop(workers_heap) #O(log(n))
        '''
        
        [min_next_free_time,next_worker]=hq.heappop(free_times_heap) #O(log(n))
        
        result.append(AssignedJob(next_worker, min_next_free_time)) #O(1)
        
       
        hq.heappush(free_times_heap,[min_next_free_time+job,next_worker]) #O(log(n))
        
        next_free_times[next_worker]=current_time+job #O(1)
            
    #ipdb.set_trace()    
    return result
    

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs_heapq(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
