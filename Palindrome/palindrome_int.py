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

import math

def palindrome(number):
    if type(number) != int:
        raise TypeError
    
    num_alt = number
    num_mod= 0
    reverse= ''
    len_num= int(math.log10(number)) + 1

    while len_num >= 1:
        num_mod= num_alt % 10
        reverse += str(num_mod)
        num_alt = int(num_alt / 10)
        len_num -= 1

    return int(reverse) == number

print(palindrome(12321))
print(palindrome(564))