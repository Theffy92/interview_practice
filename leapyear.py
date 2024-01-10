# def leapyear(year):
    
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
    
# print(leapyear(2024))

def leapyears(start_year, end_year):
    leap_years = []
    
    for year in range(start_year, end_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            leap_years.append(year)
        
    return leap_years

print(leapyears(2000, 2024))