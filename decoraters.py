# #decoraters:

# #program 1
# def decor(fun):

#   def inner(name):
#     if name=="harsh":
#       print("bad morning harsh")
#     else:
#       print("good morning ",name)
#   return inner

# @decor
# def wish(name):
#   print("good moarning ",name)


# wish("harsh")
# wish("krishna")
# #......................................

# code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner
 
def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner
 
@decor
def num():
    return 10
 
@decor1
def num2():
    return 20
   
print(num())
print(num2())


# problem 2:

# @gfg_decorator
# def hello_decorator():
#     print("Gfg")

# '''Above code is equivalent to '''

# def hello_decorator():
#     print("Gfg")
    
# gfg_decorator(hello_decorator)


#problem 3
# without using decore but it work as decorater
def decor(func):

  def inner(name):
    if name=="harsh":
      print("bad morning harsh")
    else:
      func(wish)
  return inner

def wish(name):
  print("good moarning ",name)


wish("harsh")
wish("krishna")

f=decor(wish)
f("harsh")
f("krishna")


#example 4
#
def smart_div(func):
  def nested(a,b):
    if b!=0:
      ans = func(a,b)
      return ans
    else:
      return f{""}
@smart_div
def division(a,b):
  return a/b

x,y=[int(i) for i in input().split()]
result = division(x,y)
print(result)
""" here division function is not able to divide the no. where the denominator is 0. for theat test case we get a exception zero divison error. so we need to modify that function to handle this case.
so here we define a decorator fucntion for division name of decorator is smat_div. inside it, we creat
 a nested fucntion which improve the logic for our division fucntion and at the end it get return.

 in line 97, we division is called, then python wont execute the divison becoze it has a decorator on it top(@smart_div). so python automatically called smart_div decoretor fun and pass division function as arrgument in that smart_division.
 memory address of division func is copied to func variable(func. aliasing).  it means now we are free to call divison fucntion by using func variable inside the nested fucntion. the divisio  function is replaced by the nested fucntion.
 python interpretor because this .