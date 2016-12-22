class Node(object):
    'single link list'

    def __init__(self, data, link):
        self.data = data
        self.link = link


head = None
# tail = None
# node1 = Node("A", head)
# node2 = Node("B", node1)
# node3 = Node("B", node2)
# node4 = Node("D", tail)



print("adding")
for index in range(5):
    print(index)
    head = Node(str(index), head)

print("displaying")
while head != None:
    print(head.data)
    head = head.link

print ("nextTime")

while head!=None:
	print(head.data)
	head = head.link





#
# print(node1.data)
# print(node1.link)

# while end in not None:

