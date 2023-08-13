# find factorial of a number
# def find_fact(num):
#   if num == 0:
#     return 1
    
#   return num * find_fact(num-1)

# if __name__ == '__main__':
#   num = int(input("Enter a number: "))
#   ans = find_fact(num)  
#   print("Factorial of a number: ", ans)

# to find power of a number 
# def find_power(num):
#   # base case 
#   if num == 0:
#     return 1

#   return 2 * find_power(num-1)

  # recursive relation 
  # smaller_prob = find_power(num-1)
  # bigger_prob = 2 * smaller_prob

  # return bigger_prob

# if __name__ == '__main__':
#   num = int(input("Enter a number: "))
#   ans = find_power(num)
#   print("Power of a number: ", ans)

# print n numbers 
def print_nums(num):
  # base case  
  if num == 0:
    return 

  print(num) # print in descending order (head recursion)
  print_nums(num-1)
  # print(num) # print in ascending order (tail recursion)

if __name__ == '__main__':
  num = int(input("Enter a number: "))
  print_nums(num)