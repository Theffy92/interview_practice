'''
1. Leetcode#73given a matrix of integers - mat[row][col]
write a function that will update every entry which shares a row or column with a "0" to "0"
Example:
Input:
{{0, 1, 2},  
{3, 4, 5}}         
Output:
{{0, 0, 0},
{0, 3, 5}} 
'''

# def update_matrix(matrix):
#     cols, rows = len(matrix), len(matrix[0])
#     zero_pos = []
    
#     for i in range(cols):
#         for j in range(rows):
#             if matrix[i][j] == 0:
#                 zero_pos.append((i,j))
        
#     for i, j in zero_pos:
#         for k in range(rows):
#             matrix[k][j] = 0
            
#         for k in range(cols):
#             matrix[i][k] = 0
            
#     return matrix

# matrix = [[1,2,0], [2,0,6], [0,9,1]]

# print(update_matrix(matrix))
            


'''
2.
Given a set of time intervals (started as a set of sets but changed to list of lists as
working), condense overlapping times into a single merged range, eg.
[[1,3],[2,4],[5,7],[6,8]] would become [[1,4],[5,8]]. 
Started as non-sorted but then interviewer offered to just start with sort(input) 
to make the input sorted.'''

# def time_intervals(timelist):
#     timelist.sort()
#     merged_range =[]
    
#     for i in range(0,len(timelist), 2):
#         for j in range(len(timelist[i])):
#             if timelist[i][j] < timelist[i+1][0] < timelist[i][j+1]:
#                 merged_range.append((timelist[i][j], timelist[i+1][1]))
            
#     return merged_range

# print(time_intervals([[5,7],[1,3],[6,8],[2,4]]))

'''
3.
# !!! In place. Given an array of numbers of sorted numbers, remove all duplicates from it.
# You should not use any extra space; after removing the duplicates in-place return the new 
# length of the array.

# Input: [2, 3, 3, 6, 9, 9]
# Output: 4
# [2, 3, 6, 9].

#Input: [2, 2, 2, 11]
#Output: 2
# [2, 11].
'''
# def remove_duplicates(l):
#     # l = set(l)
#     # for i in range(len(l)):
#     #     if l[i] == l[i+1]:
#     #         l.pop(i+1)
#     i = 0
#     while i < len(l) - 1:
#         if l[i] == l[i+1]:
#             l.pop(i)
#         else:
#             i +=1 
            
#     return len(l)

# print(remove_duplicates([2,3,3,6,9,9]))
# print(remove_duplicates([2,2,2,11]))

'''
4.
Given two strings, return "G" if the values at the same index match, or "B" if they don't. 
EX Input: "CRATE", "GRATE"
EX Output: "BGGGG"
EX Input: "CRATE", "SOARE"
EX Output: "BBGBG"

After solving this, was asked to return "Y" if the value was in the other word,
but just not at the same index
EX Input: "CRATE", "SOARE"
EX Output: "BBGYG"

After solving this, was asked to return an int that represents how many index values that 
letter is from the it's place in the first string. 
EX Input: "CRATE", "SOARE"
EX Output: "BBG2G"
'''
def index_match(s1,s2):
    match_s=''
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            match_s += 'G'
        elif s2[i] in s1:
            match_s += 'Y'
        else:
            match_s +='B'
            
    return match_s

print(index_match('CRATE', 'GRATE'))
print(index_match('CRATE', 'SOARE'))
'''
5.
Given a number, N, print all combinations of A/B where A is between 0 & N and B is between 1 
& N
For example:
N = 1, output: {0/1, 1/1}
N = 2, output: {0/1, 1/1, 1/2, 2/2}
N = 3, output: {0/1, 1/1, 1/2, 1/3, 2/2, 2/3, 3/3}

Then, an additional restraint was added where fractions with the same simplified values 
should not be 
added.
For example:
N = 3, output: {0/1, 1/1, 1/2, 1/3, 2/3} because 2/2 simplifies to 1/1 and 3/3 also 
simplifies to 1/1.
'''