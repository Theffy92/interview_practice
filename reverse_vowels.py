'''Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters. 

Pseudocode

1. create a variable to store all the vowels
2. get the 2 first and last letters in the string. 2 pointers
3. loop through the string 
4. check if the left pointer is a vowel and if the right pointer is a vowel
'''

def reverse_vowel(s):
    vowels= set('aeiouAEIOU')
    print(vowels)
    start, end = 0, len(s) -1
    s_list = list(s)
    
    while start < end:
        if s[start] in vowels and s[end] in vowels:
            temp=s_list[start]
            s_list[start] = s_list[end]
            s_list[end]= temp
            start += 1
            end -= 1
        elif s[start] not in vowels:
            start +=1
        elif s[end] not in vowels:
            end -=1
    # s = ''.join(s_list)
    return ''.join(s_list)

print(reverse_vowel('hello'))
    

