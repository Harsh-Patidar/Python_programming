'''
def creatmultiplier(x):
  return lambda y:x*y

multiply = creatmultiplier(10)

def execute(f,arg):
  return f(arg)

print(execute(multiply, 15))
print(execute(multiply, 25))
'''
def creatmultiplier(x):
  return lambda y:x*y

multiply = creatmultiplier(10)

def execute(f,arg):
  print("called f with " + str(arg))
  return f(arg)

print(execute(multiply, 15))
print(execute(multiply, 25))

