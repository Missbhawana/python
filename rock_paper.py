import os
os.system('cls')

dict = {}
a = "dada"
l  = len(a)
# if (a == a[::-1]) :
#     print(1)
# else :
#  for i in a:
#     if i in  dict:
#         dict[i] += 1
#     else :
#         dict[i] = 1

#  for i,j in dict.items():
#     if j > 1:
#         k = a.find(i)
#         if a[k + 1] == a[k] :
#           print(1)
#           break
#  else :
#     print(0)


def can_be_palindrome(s):
    char_count = {}
    
    # Count occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
     
    # Count how many characters occur an odd number of times
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    
    # If the string has an odd length, there can be at most one character with an odd count
    if len(s) % 2 == 1 and odd_count == 1:
        return True
    # # If the string has an even length, there shouldn't be any character with an odd count
    elif len(s) % 2 == 0 and odd_count == 0:
        return True
    else:
        return False

# Test the function
print(can_be_palindrome("dada"))
print(can_be_palindrome("abba"))