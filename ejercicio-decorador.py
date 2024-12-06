def measure_time(funcion):
  def wrapper(*args):
    import time
    start = time.time()
    result = funcion(*args)
    total = time.time() - start
    print(total, 'seconds')
    return result
  return wrapper

@measure_time
def suma(a,b):
  import time
  time.sleep(1)
  return a + b

print(suma(10, 50))
