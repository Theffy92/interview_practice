# An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the
# coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner.
# Its top and bottom edges are parallel to the X-axis, and its left and right edges are 
# parallel to the Y-axis.

# Two rectangles overlap if the area of their intersection is positive. To be clear, two 
# rectangles that only touch at the corner or edges do not overlap.

# Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise 
# return false.

# Example 1:

# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
# Example 2:

# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false
# Example 3:

# Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
# Output: false

# Constraints:

# rec1.length == 4
# rec2.length == 4
# -109 <= rec1[i], rec2[i] <= 109
# rec1 and rec2 represent a valid rectangle with a non-zero area.

#Clarifying questions
#1. Do the rectangle lists have to have an specific length of 4 in this case?
#2. Should I assume that all numbers in the rectangle lists are integers?
#3. Does the program need to check that the rectangle lists represent a valid rectangle with a
# non-zero area?

#Steps
#1. Check the rectangle lists have a length of 4.
#2. check all elements in the rectangle lists are integers and the sum of every element is 
#greater than zero.
#3. compare x2,y2 from the first rectangle against x1,y1 from the second one


def rectangle_overlap(rec1, rec2):
    if len(rec1) < 4 or len(rec2) < 4:
        return "all rectangles need 2 coordinates"
    
    is_rec1_integer = all(isinstance(x, int) for x in rec1)
    is_rec2_integer = all(isinstance(x, int) for x in rec2)

    if not is_rec1_integer or not is_rec2_integer:
        raise TypeError('invalid input types')
    
    sum_rec1 = sum(rec1)
    sum_rec2 = sum(rec2)

    if sum_rec1 == 0 or sum_rec2 == 0:
        return ('only non-zero area rectangles allowed')
    
    x2= rec1[2]
    y2 = rec1[3]
    x1= rec2[0]
    y1 = rec2[1]

    if x2 - x1 > 0 and y2 - y1 > 0:
        return True 
    return False

# rec1= [0,0,2,2]
# rec2= [1,1,3,3]
# rec1 = [0,0,1,1]
# rec2 = [1,0,2,1]
rec1 = [0,0,1,1]
rec2 = [2,2,3,3]
print(rectangle_overlap(rec1, rec2))