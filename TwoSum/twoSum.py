# Given an array of integers nums and an integer target, return indices of the two numbers such 
#that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same 
#element twice.
# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

#Clarifyng questions:
#1. can a number appear more than once in this array?
#2. is 2 the limit of numbers I should use to add up to target?
#3. should I assume that the arrays elements and the target value are integers? 
#or should my code check that and raise an error otherwise?
#4. Should I assume that the array length is greater than 1?

#pseudocode
#1. check the array and the target values are the correct data type
#2. check the array length is greater than 1
#3. create an empty dictionary to store the array elements as keys and their indices as values
#4. loop through the array and 
#4.1 create a variable inside to make a subtraction operation between 
# target and the number element we're currently looping through.
#4.2 check that the subtraction result is in the dictionary as a key already so we can return 
#the value of that key, plus the index of the current number.
#4.3 otherwise we'll add that number at the dictionary, and repeat the process in the loop
  