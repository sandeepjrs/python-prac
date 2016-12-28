#! /usr/bin/env python

class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node


class linked_list:
    def __init__(self):
        self.head = None

    def add_rear(self, data): # basically it's add to the front [null]->[adds here]->[d4]->[d3]->[d2]->[d1]
        new_node = node() # create a new node
        new_node.data = data
        new_node.next = self.head # link the new node to the 'previous' node.
        self.head = new_node #  set the current node to the new one.


    def add_front(self, data): # basically it's add to the back [startingAdd]->[d4]->[d3]->[d2]->[d1]->[adds here]
        nodes = self.head  # cant point to ll!
        while nodes:
            # print nodes.data
            if nodes.next == None:
                print("i came")
                new_node = node()
                new_node.data = data
                new_node.next = None #its a last node so always its point to null
                nodes.next = new_node # previous node now points to the new node address
                break
            nodes = nodes.next


    def add_at_index(self, index, data):
        nodes = self.head
        for i in range(0,index):
            nodes = nodes.next # got the address of the Ith position
            print("iterating ..."+str(i))

        new_node = node() # creating a new node
        new_node.data = data # putting data

        temp = nodes.next # storing previous node address in temp variable
        nodes.next = new_node #prev node address is made to new address
        new_node.next = temp # new node address is made to the prev node wich initially it was pointing to the next node


    def list_print(self):
        node = self.head # cant point to ll!
        index = 0
        while node:
            index += 1
            print (str(node.data) + "...at....index{}".format(index) )
            node = node.next


    def search(self, key):
        node = self.head # cant point to ll!

        index=0
        while node:
            index += 1
            if(key == node.data):
                print ("found")
                return index          

            node = node.next
        print ("the given is not present")








ll = linked_list()

ll.add_rear(0)
# ll.add_rear(2)
# ll.add_rear(3)
ll.add_front(-1)
ll.add_front(-2)
ll.add_front(-3)
ll.add_at_index(3,25)

# ll.search(78)
ll.list_print()