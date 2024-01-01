# Write a function named duplicates_within_k
# The function should take in an unsorted list of integers as well as an integer k
# The function should return True if any integer appears twice or more in the list within k 
# indices of each other and False if there are no duplicate integers within k indices.

# Write a function called duplicates_within_k that takes in a list of integers numbers, numbers,
# and an integer k.
# The function should return True if the same integer occurs multiple times within k distance.
# It should return False otherwise.

# For example: an input list of [1, 0, 2, 1, 3, 4] and k value 5 would return True because the 
# integer 1 occurs twice: once at index 0 and once at index 3 which is within 5 indices.

#Clarifying questions
#1.should the program contemplate getting an empty input list or an input list with just one item?
#2. should the program contemplate gettin a negative number or 0 as K value?
#3. Check if list contains integers only as well as k accepts integer only?

def duplicates_within_k(number, k):
    