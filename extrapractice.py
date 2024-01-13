'''
1.
Given a set of time intervals (started as a set of sets but changed to list of lists as
working), condense overlapping times into a single merged range, eg.
[[1,3],[2,4],[5,7],[6,8]] would become [[1,4],[5,8]]. 
Started as non-sorted but then interviewer offered to just start with sort(input) 
to make the input sorted.'''

'''
2.
# !!! In place. Given an array of numbers of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

# Input: [2, 3, 3, 6, 9, 9]
# Output: 4
# [2, 3, 6, 9].

#Input: [2, 2, 2, 11]
#Output: 2
# [2, 11].
'''

'''
3.
Given two strings, return "G" if the values at the same index match, or "B" if they don't. 
EX Input: "CRATE", "GRATE"
EX Output: "BGGGG"
EX Input: "CRATE", "SOARE"
EX Output: "BBGBG"

After solving this, was asked to return "Y" if the value was in the other word, but just not at the same index
EX Input: "CRATE", "SOARE"
EX Output: "BBGYG"

After solving this, was asked to return an int that represents how many index values that 
letter is from the it's place in the first string. 
EX Input: "CRATE", "SOARE"
EX Output: "BBG2G"
'''
'''
4.
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