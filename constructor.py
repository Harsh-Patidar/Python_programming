# class NoCon:
#   '''thsi is class has a constructor'''
#   #this default constructor is added to our class which has empty body
#   #def __init__(self):
#   #      pass
#   pass

# obj1=NoCon()
# #print(obj1.method1())  #AttributeError: 'NoCon' object has no attribute 'method1'.

# print(obj1.__init__())  #this nine genarte no error because python add a __inti__() methods automatically to our class

'''EXTRA KNOWLEDGE___

test khud me ek object hai....'''
#ye reference to the object hai...
class test:
  pass

print(test)          #----> <class '__main__.test'>
print(id(test))      #---->  2029418231584
print(type(test))    #---->  <class 'type'>