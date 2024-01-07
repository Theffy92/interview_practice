# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
 

# Example 1:

# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:

# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

# Constraints:

# 1 <= n <= 104

#Clarifying questions
#1. Should I assume that the users is always input an integer?
#2. does the n value has a constaint?

#Steps
#1. Check if n is actually an integer greater than 0
#2. Create an empty list
#3. loop n times and in this iteration check if the current n[i] number we're in is divisible by 3 and 5
#add FizzBuzz to the list
#3.1 if not check if it is divisible by 3 add Fizz to the list
#3.2 if not check if it is divisible by 5 add Buzz to the list
#else add the current number as a string in the list

def fizzbuzz(n):
    if type(n) != int:
        raise TypeError('Invalid input. Must be an integer')
    
    string_list = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            string_list.append('FizzBuzz')
        elif i % 3 == 0:
            string_list.append('Fizz')
        elif i % 5 == 0: 
            string_list.append('Buzz')
        else:
            string_list.append(str(i))
            
    return string_list

print(fizzbuzz(10))