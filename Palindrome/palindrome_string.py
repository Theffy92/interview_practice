def palindrome(word):
    start, end = 0, len(word)-1
    
    while start < end:
        if word[start] == word[end]:
            start +=1
            end-=1
        else:
            return False
        
    return True

print(palindrome("level"))