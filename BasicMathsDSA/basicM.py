# check whether the number is prime or not 
def find_prime(num):
  if num <= 1:
    return "Number is not a prime number"
  elif num > 1:
    for i in range(2, num-1):
      if num%i == 0:
        return "Number is not a prime number."
      else:
        return "Number is a Prime Number"

print(find_prime(7))