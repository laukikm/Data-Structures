# python3
#Solution by Laukik Mujumdar

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts: #O(n) 
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)): #O(n)
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts: #O(n)
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

def process_queries_direct_addressing(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    #Each number has 7 digits. So we need an array of 10^7 capacity
    for i in range(10**7): #O(10^7)
        contacts.append('not found')
    
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            index=cur_query.number
            contacts[index]=cur_query.name #This is O(1), since python uses dynamically allocated arrays instead of linked lists1
            
        elif cur_query.type == 'del':
            index=cur_query.number
            contacts[index]='not found'
        else:
            response = contacts[cur_query.number]
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries_direct_addressing(read_queries()))

