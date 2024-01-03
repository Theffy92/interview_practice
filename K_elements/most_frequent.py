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

def most_frequent_k_elements(nums, k):
    is_nums_int = all(isinstance(num, int) for num in nums)

    if not is_nums_int or not isinstance(k, int):
        raise TypeError('invalid input type')
    
    if k >= len(nums):
        raise ValueError('k can not be greater than the length of the array')
    
    nums_sort = sorted(nums, key= nums.count, reverse=True)
    print(nums_sort)
    freq_dict = {}
    kth_list = []
    for num in nums_sort:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

        if freq_dict[num] == k and num not in kth_list:
            kth_list.append(num)

    return kth_list

print(most_frequent_k_elements([1,2,5,1,-1,3,4,-1,3,3], 2))
