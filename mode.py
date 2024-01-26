'''
Given a list of numbers, find the mode of the set. 
Ex: given: [7,3,5,8,3,6,1,3,4,5], mode: 3
The number 3 occurs three times in this set of integers. This is more than any other integer, so the mode is 3. 
- Asked about edge cases after
'''

def find_mode(nums):
    is_nums_int = all(isinstance(num, int) for num in nums)
    
    if not is_nums_int or len(nums) <=1:
        return 'all numbers must be integers or the length of numbers must be greater than 1'
    
    dict_nums={}
    
    for num in nums:
        if num in dict_nums:
            dict_nums[num] += 1
        else:
            dict_nums[num] = 1
    maxvalue= 0
    mode = 0
   
    for num, count in dict_nums.items():
        if count > maxvalue:
            maxvalue = count
            mode = num
            
    return mode

print(find_mode([7,3,5,8,3,6,1,3,4,5]))
    
    