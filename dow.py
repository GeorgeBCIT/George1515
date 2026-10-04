month_codes = {'January': 1, 'February': 4, 'March': 4, 'April': 0, 'May': 2, 'June': 5, 'July': 0, 'August': 3, 'September': 6, 'October': 1, 'November': 4, 'December': 6}
day_codes = {0: 'Saturday', 1: 'Sunday', 2: 'Monday',  3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday'}
def isLeapYear(year):
    if year % 400 == 0:
        return(True)
    elif year % 100 == 0:
        return(False)
    elif year % 4 == 0:
        return(True)
    return False    
def getDayOfTheWeek(year, month, day):
    year_last_two_digits = year % 100
    step_one_result = year_last_two_digits // 12
    step_two_result = year_last_two_digits % 12
    step_three_result = step_two_result // 4
    step_four_result = step_one_result + step_two_result + step_three_result + day + month_codes[month]
    step_five_result = step_four_result % 7 
    if isLeapYear(year) == True:    
        if 1600 <= year <= 1699:
            if month == 'January' or month == 'February':
                return day_codes[((step_four_result - 1 + 6) % 7)]
            elif month != 'January' and month != 'February':
                return day_codes[((step_four_result + 6) % 7)]  
        elif 1700 <= year <= 1799:
            if month == 'January' or month == 'February':
                return day_codes[(step_four_result - 1 + 4) % 7]
            elif month != 'January' and month != 'February':
                return day_codes[(step_four_result + 4) % 7]   
        elif 1800 <= year <= 1899:
            if month == 'January' or month == 'February':
                return day_codes[(step_four_result - 1 + 2) % 7]
            elif month != 'January' and month != 'February':
                return day_codes[(step_four_result + 2) % 7]
        elif 1900 <= year <= 1999:
            if month == 'January' or month == 'February':
                return day_codes[(step_four_result - 1) % 7]
            elif month != 'January' and month != 'February':
                return day_codes[step_four_result % 7]          
        elif 2000 <= year <= 2099:
            if month == 'January' or month == 'February':
                return day_codes[(step_four_result - 1 + 6) % 7]
            elif month != 'January' and month != 'February':
                return day_codes[(step_four_result + 6) % 7] 
        elif 2100 <= year <= 2199:
            if month == 'January' or month == 'February':
                return day_codes[(step_four_result - 1 + 4) % 7]
            elif month != 'January' and month != 'February':
                return day_codes[(step_four_result + 4) % 7]
    else:
        if 1600 <= year <= 1699:
            return day_codes[(step_four_result + 6) % 7]  
        elif 1700 <= year <= 1799:
            return day_codes[(step_four_result + 4) % 7]   
        elif 1800 <= year <= 1899:
            return day_codes[(step_four_result + 2) % 7] 
        elif 1900 <= year <= 1999:
            return day_codes[step_four_result % 7]
        elif 2000 <= year <= 2099:
            return day_codes[(step_four_result + 6) % 7] 
        elif 2100 <= year <= 2199:
            return day_codes[(step_four_result + 4) % 7]

 