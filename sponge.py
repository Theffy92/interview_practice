"""
Create a function that takes a string consisting of one or more words separated by spaces. It should return a new string converted to "sponge case," where each word
 starts with a lowercase letter, and then alternates between upper and lower case for each following letter in the word.

Examples:

sponge_case("spongebob") # Should return "sPoNgEbOb"

sponge_case("Who are YOU calling A Pinhead") # Should return "wHo aRe yOu cAlLiNg a pInHeAd"

sponge_case("WHAT is UP my dude") # Should return "wHaT iS uP mY dUdE"

sponge_case("E") # Should return "e"

sponge_case("e") # Should return "e"

1. taking care of the type erros and that the string only has letters and blanks.
2. separate every word using other variable to make sure every word actually starts with lower case letter
2.1 looping through every word and alternate lower and upper case
3. add every word into a new string with the modify word cases
"""
import re

def sponge_case(sentence):
    # Write your solution here!
    if not bool(re.match('[a-zA-Z\s]+$', sentence)):
        return "sentence must have only letters and blanks"
    
    sentence_split = sentence.split()
    sponge_sentence_list = []
    
    for i in range(len(sentence_split)):
        sponge_sentence_str = ''
        for j in range(len(sentence_split[i])):
            if j%2==0:
                lower_case_letter = sentence_split[i][j].lower()
                sponge_sentence_str += lower_case_letter
            else:
                upper_case_letter = sentence_split[i][j].upper()
                sponge_sentence_str += upper_case_letter
        sponge_sentence_list.append(sponge_sentence_str)
    
    sponge_sentene = " ".join(sponge_sentence_list)
    print(sponge_sentene)

    return sponge_sentene

# Test cases
assert sponge_case("mi34r6?") == "sentence must have only letters and blanks"
assert sponge_case("spongebob") == "sPoNgEbOb"
assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
assert sponge_case("E") == "e"
assert sponge_case("e") == "e"
print('All test passed')