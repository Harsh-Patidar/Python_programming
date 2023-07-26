import time

def log_performacne(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"function'{func.__name__}'took{execution_time:4f} seconds to execute.")
    return result
  return wrapper

@log_performacne
def calculate_total():
  total = 0
  for i in range(1,1000001):
    total += 1
  return total