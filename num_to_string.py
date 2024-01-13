'''
Num to text; i.e. input = 3 output = "three"
'''

def num_to_text(num):
    num_map= {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}
    
    for n, text in num_map.items():
        if num == n:
            return text
        
        
print(num_to_text(3))