# check whether the number is neon number or not 

def check_neon(num):
  sum = 0
  original = num 
  square = num ** 2

  while square > 0:
    reminder = square % 10 
    sum += reminder
    square //= 10 
  
  if sum == original:
    return "Neon Number."
  else:
    return "Not Neon Number."

print(check_neon(1))