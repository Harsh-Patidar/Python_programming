# function:
'''def multiply(x,y):
  return x * y

print(multiply(10,15))
'''
#lambda function(anonymous fn i.e. without name)
multiply = lambda x,y:x*y
print( multiply(64,2),end=',')
print(multiply(500,5))

# # 
# def creatmultiplier(x):
#   return lambda y:x*y

# multiply = creatmultiplier(10)

# print(multiply(15),end=',')
# print(multiply(25))