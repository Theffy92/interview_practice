#nurses run , race car, mom, dad
#is it case sensitive?

#1- check if the value is a string
#2- if the string is formed by more than 1 word and it has blanks, 
# I would remove the blanks
#3- reverse the word and store it in a new variable
#4- compare the reverse string with the actual string

# def palindrome(string):
#     if type(string) != str:
#         raise TypeError
#     print(string)
#     new_string = ""
#     for char in string:
#         if char != " ":
#             new_string += char
            
#     string = "".join(new_string)
    
#     rev_string = new_string[::-1]
#     print("string now is: " + string)
#     print("reverse is:" + rev_string)
#     return rev_string == string

# print(palindrome("nurses run"))

def palindrome(string):
    if type(string) != str:
        raise TypeError
    
    string_lower= string.lower()
    word_no_blanks = ""
    for char in string_lower:
        if char != " ":
            word_no_blanks += char
            
    string_lower = "".join(word_no_blanks)
    print(string_lower)
    rev_string = string_lower[::-1]
    
    return rev_string == string_lower

print(palindrome("Race cAr"))
print(palindrome("mOm"))