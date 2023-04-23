# #Here's an example of a generator function that produces a sequence of numbers
# def my_generator(n):
#   value = 0
#   while value < n:
#     yield value
#     value = value+1
    
# n=int(input())
# for value in my_generator(n):
#   print(value)

# #Generator Expression Syntax
# #   (expression for item in iterable)

# #Example 2: Python Generator Expression
# square_generator = (i*i for i in range(5))

# for i in square_generator:
#   print(i)

# #output:-
# # 0
# # 1
# # 4
# # 9
# # # 16

# # Infinite list of prime numbers using Python generators........

def prime_generator():
  n=2
  while True:
    n=n+1
    yield n

generator = prime_generator()
for i in range(10):
  print(next(generator))

