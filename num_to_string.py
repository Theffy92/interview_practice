'''
Num to text; i.e. input = 3 output = "three"
'''

def num_to_text(num):
    num_map= {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6: 'six', 7: 'seven',
              8: 'eight', 9:'nine', 10:'ten'}
    
    if num <= 10:
        return num_map[num]
    
    if 10 < num < 100:
        
        tens_digit = num // 10
        unit_digit = num % 10
        text_unit = num_map[unit_digit]
        text_tens = num_map[tens_digit]
        if num < 20:
            if text_unit == 'four' or text_unit == 'six' or text_unit == 'seven' or text_unit == 'eight' or text_unit == 'nine':
               return f"{text_unit}teen"
            elif text_unit== 'one':
                return "eleven"
            elif text_unit == 'two':
                return "twelve"
            elif text_unit == 'three':
                return "thirteen"
            elif text_unit == 'five':
                return "fifteen"
        else:
            if text_tens == 'six' or text_tens == 'seven' or text_tens == 'eight' or text_tens == 'nine':
                return f"{text_tens}ty{ '-' + text_unit if unit_digit!= 0 else ''}"
            elif text_tens == 'two':
                return f"twenty{'-' + text_unit if unit_digit != 0 else ''}"
            elif text_tens == 'three':
                return f"thirty{'-' + text_unit if unit_digit != 0 else ''}"
            elif text_tens == 'four':
                return f"forty{'-' + text_unit if unit_digit != 0 else ''}"
            elif text_tens == 'five':
                return f"fifty{'-' + text_unit if unit_digit != 0 else ''}"
        
print(num_to_text(57))