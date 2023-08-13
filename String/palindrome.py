# def check_palindrome(st):
#   rev = ""

#   for i in st:
#     rev = i + rev

#   if rev == st:
#     print("String is palindrome")
#   else:
#     print("String is not a palindrome.")


# check_palindrome("hihi")

# def check_palindrome(st):
#   temp = ""
#   for i in st:
#     if i.isalpha() or i.isdigit():
#       temp += i.lower()

#   # return temp

#   l, r = 0, len(temp)-1
#   while l <= r:
#     if temp[l] != temp[r]:
#       return False
#     else:
#       l += 1
#       r -= 1

#   return True


# print(check_palindrome("11!Aa11@"))