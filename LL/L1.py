# Single Linked list:
class Node:
  def __init__(self, data):
    self.data = data
    self.ref = None
node1 = Node(10)    # here node is created [10|None]
print(node1)

class Linkedlist:
  def __init__(self):
    self.head = None
  def print_LL(self):
    if self.head is None:
      print("linked list is empty")
    else:
      n = self.head
      while n is not None:
        print(n.data,"--->", end=" ")
        n= n.ref
#adding new node at beginning...

  def add_begin(self,data):
    new_node = Node(data)
    new_node.ref = self.head
    self.head = new_node

#adding new node at last........
  def add_end(self,data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      n = self.head
      while n.ref is not None:
        n= n.ref
      n.ref = new_node


ll1 = Linkedlist()
ll1.add_begin(10)
ll1.add_end(999)
ll1.add_end(900)
ll1.add_begin(20)
ll1.print_LL()
 

