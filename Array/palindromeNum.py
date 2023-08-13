def find_palindrome(num):

  left, right = 0, len(num)-1 

  while left <= right:
    if num[left] == num[right]:
      return True 
    
    else:
      return False 

    left += 1
    right -= 1
  

if __name__ == '__main__':
  res = find_palindrome("aaa")

  if res:
    print("Palindrome number.")
  else:
    print("Not palindrome number.")