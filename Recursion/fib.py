# Find nth fibonacci

def find_fib(num):
  if num <= 1:
    return num  

  res1 = find_fib(num-1)
  res2 = find_fib(num-2)

  return res1 + res2 

if __name__ == '__main__':
  num = int(input("Enter a number: "))
  print("Fibonacci series: ", find_fib(num))