'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.'''

#I will create a list variable to use it as a stack 
# and work with the LIFO theory to check if every open ang closing parentheses matches
# For this I will also create a dictionary that store the closing parentheses as keys and 
# the open parentheses

# def valid_parentheses(s):
#     stack= []
#     #brackets_map = {')':'(', '}':'{', ']':'['}
    
#     # for char in s:
#     #     if char in bracket_map.values():
#     #         stack.append(char)
#     #     elif char in bracket_map.keys():
#     #         if not stack or stack.pop() != bracket_map[char]:
#     #             return False
#     #     else:
#     #         return False
#     brackets_map = {'(':')', '{':'}', '[':']'}
    
#     for char in s:
#         if char in brackets_map.keys():
#             stack.append(char)
#         elif char in brackets_map.values():
#             if not stack or stack.pop() != list(brackets_map.keys())[list(brackets_map.values()).index(char)]:
#                 return False
#         else:
#             return False

#     return not stack

# print(valid_parentheses('()[]')) #True
# print(valid_parentheses('()[')) #False
# print(valid_parentheses(']{}[]')) #False