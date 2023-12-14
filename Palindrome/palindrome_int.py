#1- check that the value is actually an integer
#2- create new variables that I'll use in the while loop
# counter to store the length of the number, a reverse variable, a num_mod variable, a variable to 
#store a copy of the number
#3- While loop until counter >= 1
   #3.1- num_mod mod 10
   #3.2- add the num_mod result to the reverse string variable
   #3.4- taking the last digit out of the num_alt (number's copy)
   #3.5- decrease the counter by 1
#4- convert the reverse result into integer
#5- compare reverse with number and if they match then it's True
#otherwise is False

# import math

# def palindrome(number):
#     if type(number) != int:
#         raise TypeError
    
#     num_alt = number
#     num_mod= 0
#     reverse= ''
#     len_num= int(math.log10(number)) + 1

#     while len_num >= 1:
#         num_mod= num_alt % 10
#         reverse += str(num_mod)
#         num_alt = int(num_alt / 10)
#         len_num -= 1

#     return int(reverse) == number
import math 

# def palindrome(number):
#     if type(number) != int:
#         raise TypeError
    
#     #A logarithm (of the base b) is the power to which the base needs to be raised to 
#     # yield a given number.
#     #it's gonna be rounded down
#     counter_len =int(math.log10(number)) + 1
#     number_copy = number
#     reverse = ""
#     rev_mod = 0
#     while counter_len >= 1:
#         rev_mod = number_copy % 10
#         reverse += str(rev_mod)
#         number_copy = int(number_copy/10)
#         counter_len -= 1
        
#     return int(reverse) == number
    

#recursive
def is_palindrome_recursive(number):
    #base case: number has one digit or zero
    counter_len = int(math.log10(number)) + 1
    if counter_len <= 1:
        return True
    
    rev_mod = number % 10
    number_copy = int(number / 10)
    
    return rev_mod == number_copy % 10 and is_palindrome_recursive(number_copy)
  
    
# print(palindrome(12321))
# print(palindrome(121))
# print(palindrome(564))
print(is_palindrome_recursive(1232))

#I've finished in less than 20 min (pseudocode included)