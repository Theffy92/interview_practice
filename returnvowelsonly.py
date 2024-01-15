#Given a string return vowels only

def vowels_only(s):
    vowels_set = set('aeiouAEIOU')
    vowels_list = []
    index = 0
    while index <= len(s)-1:
        if s[index] in vowels_set and s[index] not in vowels_list:
            vowels_list.append(s[index])
            index += 1
        else:
            index += 1
            
    return ''.join(vowels_list)

print(vowels_only('hola que tal'))
print(vowels_only('vowels everywhere'))