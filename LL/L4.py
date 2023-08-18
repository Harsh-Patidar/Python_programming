class Node:
  def __init__(self,data):
    self.data = data
    self.ref = None
  
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
        n =n.ref

#adding new node at begning
  def add_begin(self,data):
    new_node = Node(data)
    new_node.ref = self.head
    self.head = new_node

#adding new node at end
  def add_end(self,data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      n = self.head 
      while n.ref is not None:
        n = n.ref 
      n.ref = new_node
    
  #adding new node at position



ll1 =  Linkedlist()
ll1.add_begin(25)
ll1.add_begin(20)
ll1.add_end(33)
ll1.add_end(67)
ll1.print_LL()