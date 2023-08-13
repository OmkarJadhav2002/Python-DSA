# check whether the number is palindrome or not 

def check_palindrome(num):
  number = str(num)
  l, r = 0, len(number)-1

  while l < r:
    if number[l] != number[r]:
      return "Not palindrome number"

    l += 1
    r -= 1

  return "Palindrome number."


print(check_palindrome(12))