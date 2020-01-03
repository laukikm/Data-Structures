# python3
#Solution by Laukik Mujumdar
#import ipdb
class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []
        self.hash_table=[]
        for i in range(self.bucket_count):
            self.hash_table.append([])
        
    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_query_hash_table(self,query):
        if query.type == "check":
            index=query.ind
            l=self.hash_table[index]
            l.reverse()
            print(' '.join(l)) #Print the list with spaces
            l.reverse()
        else:
            hash_value=self._hash_func(query.s)
            if query.type == 'find':
                if(query.s in self.hash_table[hash_value]):
                    print('yes')
                else:
                    print('no')
            elif query.type == 'add':
                if(query.s in self.hash_table[hash_value]):
                    pass
                else:
                    #ipdb.set_trace()
                    self.hash_table[hash_value].append(query.s)
            elif query.type=='del':
                if(query.s in self.hash_table[hash_value]):
                    self.hash_table[hash_value].remove(query.s)
                    
                
    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())
    
    def process_queries_stress_test(self,artificial_queries):
        n=len(artificial_queries)
        for i in range(n):
            self.process_query(artificial_queries[i])
        
    def process_queries_hash_table(self):
        n = int(input())
        for i in range(n):
            self.process_query_hash_table(self.read_query())
            

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries_hash_table()
