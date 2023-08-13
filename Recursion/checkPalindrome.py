def checkPalindrome(s, start, end):

  # using recursion
  # base case 
  if start > end:
    return True

  if s[start] != s[end]:
    return 0
  else:
    return checkPalindrome(s, start+1, end-1)
  # start, end = 0, len(s)-1

  # while start <= end:
  #   if s[start] != s[end]:
  #     return 0

  #   else:
  #     start += 1
  #     end -= 1

  # return 1

if __name__ == '__main__':
  s = "aba"
  res = checkPalindrome(s, 0, len(s)-1)
  if res == 0:
    print("String is not a palindrome.")
  else:
    print("String is a palindrome.")