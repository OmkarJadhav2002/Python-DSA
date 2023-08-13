# find prime numbers between n 

def find_prime_nums(nums):
  res = []

  for num in range(nums):
    if num > 1:
      for j in range(2, num):
        if num%j == 0:
          break 
      else:
        res.append(num)
  
  return res 

print(find_prime_nums(10))
# check whether the number if prime or not 

# def check_prime(num):
#   if num < 2:
#     print("Not a prime number.")

#   else:
#     for i in range(2, num):
#       if num % i == 0:
#         print(num, "Not a prime number.")
#         break 
#     else:
#       print(num, "is Prime number.")

# check_prime(11)