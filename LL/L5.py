class Node:
  def __init__(self,data):
    self.data = data
    self.ref = None

class linkedlist:
  def __init__(self):
    self.head = None
  
  def print_LL(self):
    if self.head is None:
      print("linked list is empty")
    else:
      n=self.head
      while n is not None:
        print(n.data)
        n=n.ref
  
#adding new node at begining


