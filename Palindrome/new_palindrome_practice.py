#taking care of negative numbers too

#import math

# def palindrome(num):
#     if not isinstance(num, int):
#         raise TypeError('Invalid input type')
    
#     if num == 0:
#         return True
    
#     #the length of digits in the number
#     len_num = len(str(abs(num)))
#     # len_num = int(math.log10(abs(num))) + 1
#     # num_rev = ' '
#     num_rev = 0
#     modulo = 0
#     count = 0
#     num_copy = num
    
#     while count < len_num:
#         modulo = num_copy % 10
#         num_rev = num_rev * 10 + modulo
#         # num_rev += str(modulo) 
#         num_copy = int(num_copy / 10)
#         count +=1
        
#     return num_rev == num

def is_palindrome(num):
    len_num = len(str(abs(num)))
    mod = 0
    rev = 0
    num_alt = num
    
    while len_num >= 1:
        mod = num_alt % 10
        rev = rev * 10 + mod
        num_alt = num_alt // 10
        len_num -= 1
    
    return rev == num

print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(1))
#print(palindrome(-525))