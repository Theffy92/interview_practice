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

# def duplicates_within_k(numbers, k):
#     is_integer_lst = all(isinstance(x, int) for x in numbers)
#     # print(is_integer_lst)
#     if is_integer_lst == False or type(k) != int:
#         raise TypeError
    
#     if len(numbers) > 1 and k >= 1:
#         for i in range(len(numbers)):
#             j= i + 1
#             distance_left= k
#             while distance_left > 0 and j < len(numbers):
#                 if numbers[i] == numbers[j]:
#                     return True
#                 j+=1
#                 distance_left -=1
 
            
#     return False

#implementing using dictionary

# Say we have an input list [1, 0, 2, 1, 3, 4] and k value of 5. We could generate the
# dictionary:

# {
#   0: [1],
#   1: [0, 3],
#   2: [2],
#   3: [4],
#   4: [5]
# }
# In the dictionary above the key is an element occurring in the input list and the value is a 
# list of indices at which that element occurs.

# We can see that the key 1 has multiple indices paired with it - 0 and 3 - indicating that it 
# occurs in our input list at least twice.

# If we find the difference between the two indices 3-0=3 we will find that 3 < 5 where 5 is 
# the value of k. Thus we can see that the value 1 occurs multiple times within the distance k.

# To make our hash table, we'll only have to look at each element in the list once, so this 
# approach should be more efficient than our original solution!
def duplicates_within_k(numbers, k):
    is_integer_numbers= all(isinstance(x, int) for x in numbers)
    
    if is_integer_numbers == False or type(k)!= int:
        raise TypeError('no integer')
    
    if len(numbers) >= 2 and k>=1:
        new_dict = {}
        for i in range(len(numbers)):
            if numbers[i] not in new_dict:
                new_dict[numbers[i]] =[i]
            else:
                new_dict[numbers[i]].append(i)
                
        print(new_dict)
    
print(duplicates_within_k([1, 0, 2, 1, 3, 4], 5))
# print(duplicates_within_k([1,2], 1))

