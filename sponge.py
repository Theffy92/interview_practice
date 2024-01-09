"""
Create a function that takes a string consisting of one or more words separated by spaces. It should return a new string converted to "sponge case," where each word starts with a lowercase letter, and then alternates between upper and lower case for each following letter in the word.

Examples:

sponge_case("spongebob") # Should return "sPoNgEbOb"

sponge_case("Who are YOU calling A Pinhead") # Should return "wHo aRe yOu cAlLiNg a pInHeAd"

sponge_case("WHAT is UP my dude") # Should return "wHaT iS uP mY dUdE"

sponge_case("E") # Should return "e"

sponge_case("e") # Should return "e"
"""

def sponge_case(sentence):
    # Write your solution here!
    pass

# Test cases
assert sponge_case("spongebob") == "sPoNgEbOb"
assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
assert sponge_case("E") == "e"
assert sponge_case("e") == "e"