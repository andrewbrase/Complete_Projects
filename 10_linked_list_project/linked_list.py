# class Node to create node obj in linked list
class Node:
    def __init__(self,data=None):
        '''takes in data and creates node obj with data and with next pointer for linked list'''
        self.data = data
        self.next = None

# linked list data structure
class LinkedList:
    def __init__(self):
        '''creates empty linked list with head and tail = None'''
        self.head = None
        self.tail = None
    
    def add_node(self,data):
        '''takes in data to append to end of linked list'''
        new_node = Node(data) # creates new obj with data
        
        if self.head is None: # if there are no other nodes in linked list
            # head and tail are set to data
            self.head = new_node
            self.tail = new_node
            return f'{data} has been added to linked list'
        else: # if there are pre-existing nodes within the linked list
            # data is added to tails pointer next
            self.tail.next = new_node
            # tail is set to data
            self.tail = new_node
            return f'{data} has been added to linked list'
    
    def prepend(self,data):
        '''takes in data to prepend to beginning of linked list'''
        new_node = Node(data) # creates new obj with data

        # sets the data's pointer to the head of the linked list
        new_node.next = self.head
        # sets the head to the data
        self.head = new_node
        return f'{data} has been added to the beginning of linked list'

    def delete(self,data):
        '''takes in data to delete from linked list'''
        # creates current_node from head of linked list
        current_node = self.head

        if current_node is None: # if head is None:
            return 'no data in linked list to remove'

        if current_node.data == data: # if the head of the linked list is equal to the desired delete param:
            # the head is set to the heads pointer
            self.head = current_node.next
            return f'{data} deleted from beginning of linked list'

        while current_node.next is not None: # while current_node's (starting at head) pointer is not None (will go until end of linked list)
            if current_node.next.data == data: # if pointers data == delete param:
                current_node.next = current_node.next.next # pointer = pointer's pointer
                return f'{data} deleted from linked list'
            current_node = current_node.next # iterates through nodes 

    def insert(self, prev_value, data):
        '''takes in data and position to insert after a given node'''
        current_node = self.head # sets current node to th head of the linked list

        if current_node is None: # if linked list is empty
            return

        new_node = Node(data) # creates new obj with data

        while current_node is not None:
            if current_node.data == prev_value: # if current node is equal to the value specified in pre_val

                # Insert the new node after the current node
                new_node.next = current_node.next
                current_node.next = new_node

                if new_node.next is None: # if no tail after inserted value, make inserted value the tail
                    self.tail = new_node
                else:
                    # Update the prev reference of the node that is being inserted after the current node
                    new_node.next.prev = new_node
                # Print the location where the data was inserted
                return f'{data} inserted after {current_node.data}'

            current_node = current_node.next # iterates through nodes 
        return f'Could not find {prev_value} in Linked List'

    def print_all(self):
        '''prints off all nodes in linked list'''
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

# create linked list obj
my_linked = LinkedList()

print(my_linked.delete('start w/ no data'))
# --> no data in linked list to remove

my_linked.add_node('test delete')
print(my_linked.delete('test delete'))
# test delete deleted from beginning of linked list

# testing add node method
my_linked.add_node('A')
my_linked.add_node('B')
my_linked.add_node('C')
print(my_linked.add_node('D'))
# --> D has been added to linked list

# testing prepend and delete method
print(my_linked.prepend('first'))
my_linked.delete('first')

# creating a method to insert data after a specific node pointer
my_linked.insert('D','E')
print(my_linked.insert('E','F'))

# if value entered to insert after not in list
print(my_linked.insert('Andrew','G'))
# --> Could not find Andrew in Linked List

print(my_linked.delete('F'))
# --> F deleted from linked list

my_linked.print_all()
#  --> A B C D E 