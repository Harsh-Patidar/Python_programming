# #decorator chaining...

# #example 1

def decor2(func):
  def wrap(name):
    print("decor2 execution")
    func(name)
  return wrap

def decor1(func):
  def wrap(name):
    print("decor1 execution")
    func(name)
  return wrap


@decor1
@decor2
def wish(name):
  print("hello",name,"good morning")

wish("harsh")

# #example2

def decor1(func):
  def wrap():
    print("decor1 execution")
    func(name)
  return wrap

def decor2(func):
  def wrap():
    print("decor2 execution")
    func(name)
  return wrap  

def decor3(func):
  def wrap():
    print("decor3 execution")
    func(name)
  return wrap

@decor1
@decor2
@decor3
def func():
  print("this code is executed")

# func()

# #example 3

def starwala(func):
  def nested():
    print("********")
    func()
    print("AAAA")
  return nested

def haswala(func):
  def nested():
    print("######")
    func()
    print("#!#!#!")
  return nested

@starwala                 #it is not possibe to apply decorator simultaneously,...on multiple function
@haswala                      #aagr yaha bhi starwala kr de tho
def greet():
  print("heel")

def treat():
  print("gice")
greet()
treat()

# #Example 4
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
 
@decor1
@decor
def num():
    return 20
 
print(num())