# def most_frequent_k_elements(nums, k):
#     is_nums_int = all(isinstance(num, int) for num in nums)

#     if not is_nums_int or not isinstance(k, int):
#         raise TypeError('invalid input type')
    
#     if k >= len(nums):
#         raise ValueError('k can not be greater than the length of the array')
    
#     nums_sort = sorted(nums, key= nums.count, reverse=True)
#     print(nums_sort)
#     freq_dict = {}
#     kth_set = set()
#     for num in nums_sort:
#         if num in freq_dict:
#             freq_dict[num] += 1
#         else:
#             freq_dict[num] = 1

#         if freq_dict[num] >= k:
#             kth_set.add(num)

#     return list(kth_set)

# def most_frequent_k_elements(nums, k):
#     # Check if all elements in nums are integers
#     is_nums_int = all(isinstance(num, int) for num in nums)

#     # Check if k is an integer
#     if not is_nums_int or not isinstance(k, int):
#         raise TypeError('invalid input type')
    
#     # Check if k is greater than or equal to the length of nums
#     if k >= len(nums):
#         raise ValueError('k can not be greater than the length of the array')
    
#     # Sort nums based on frequency in descending order
#     nums_sort = sorted(nums, key= nums.count, reverse=True)

#     print(nums_sort)
#     # Initialize a dictionary to store the frequency of each element
#     freq_dict = {}
#     # Initialize a list to store the kth most frequent elements
#     kth_list = []
#     # Iterate through sorted nums to count frequencies and identify kth most frequent elements
#     for num in nums_sort:
#         # Update the frequency count in the dictionary
#         if num in freq_dict:
#             freq_dict[num] += 1
#         else:
#             freq_dict[num] = 1
#         # Check if the frequency is equal to k and the element is not already in the kth_list
#         if freq_dict[num] == k and num not in kth_list:
#             kth_list.append(num)

#     # Return the list of kth most frequent elements
#     return kth_list



def most_frequent_k_elements(nums, k):
    # Check if all elements in nums are integers
    is_nums_int = all(isinstance(num, int) for num in nums)

    # Check if k is an integer
    if not is_nums_int or not isinstance(k, int):
        raise TypeError('invalid input type')

    # Check if k is greater than or equal to the length of nums
    if k >= len(nums):
        raise ValueError('k cannot be greater than or equal to the length of the array')

    # Dictionary to store the frequency of each element
    freq_dict = {}

    # Set to store elements that appear k times or more
    kth_set = set()

    # Iterate through nums to count frequencies
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

        # Check if the current element appears k times or more
        if freq_dict[num] == k:
            kth_set.add(num)

    return list(kth_set)

print(most_frequent_k_elements([1,2,5,1,-1,3,4,-1,3,3], 2))

