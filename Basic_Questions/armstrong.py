# Check whether the number is armstrong number or not 

def check_armstrong(num):
  length = len(str(num)) 
  original = num 
  sum = 0 

  while num > 0:
    reminder = num % 10 
    sum += reminder**length 
    num //= 10 

  if original == sum:
    print("Number is armstrong number.")

  else:
    print("Number is not armstrong number.")

check_armstrong(123)