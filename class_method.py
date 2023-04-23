# # why we need class method if we allready using instance method

# CLASS METHOD:
# =============
class emp:
  def __init__(self):
    c=input()
    Emp.cmp_name=c 
obj1=Emp()   ----> cmp_name cl ass variable get created with value google




# CREATION----
# =============
# @classmethod(----->Decorators)
# def class_method(cls,......)
#   //code ---> we can only apply class variable
# Class_name.class_method()

# >>just like cconstructor and instance method, class method also have a special argunment at first position.
# >>the parameter of class method is pointing to CLASS OBJECT


"""
class Test:
  count = 0
  def __init__(self):
    Test.count+=1
  @classmethod
  def display(cls):
    print("the,",cls.count)
  
obj=Test()
obj=Test()
Test.display()
obj=Test()
obj=Test()
Test.display()

"""
"""
class Myclass:
  @classmethod
  def demo(cls):
    print("this is the")
    print("cls:-",cls)
  
Myclass.demo()
obj=Myclass()
obj.demo()
obj.demo()
obj.demo()
"""


"""NOTE**
we can also call our class method using object refn. but it is not recommanded because it may cause some unexpected behviours. it is not even more readable and confusing tooo.
in 99.9% case we can correct output but in few case we might get unexpected output....
"""

#create student class with few instance variable like --> ID, NAME, AGE
#create some method