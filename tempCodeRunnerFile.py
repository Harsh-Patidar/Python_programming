def prime_generator():
  n=2
  while True:
    n=n+1
    yield n

generator = prime_generator()
for i in range(10):
  print(next(generator))
