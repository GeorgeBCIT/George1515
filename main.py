import dow

year_fixed = 2026
def makeCalendar():
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for month in range(12):
        for day in range(1, days_per_month[month] + 1):
            print(f'{(month + 1)}-{day}-{year_fixed} is a {dow.getDayOfTheWeek(year_fixed, months[month], day)}')

def getDayOfTheWeekForUserDate():
    while True:
        User_Year = input('Please Enter a Year: ')
        if not User_Year.isdigit():
            print('Year has to be a number, please retry')
            continue
        User_Year = int(User_Year)
        if User_Year < 0:
            print('Year cannot be negative, please retry')
            continue
        break
    while True:    
        User_Day = input('Please Enter a Day: ')
        if not User_Day.isdigit():
            print('The Day has to be a number, please retry')
            continue
        User_Day = int(User_Day)
        if User_Day < 0:
            print('The Day cannot be negative, please retry')
            continue
        break
    while True:   
        User_Month = input('Please Enter a Month: ')
        if User_Month.isnumeric() or (User_Month not in dow.month_codes):
            print('Month must correspond to the appropriate word, please retry')
            continue
        break
    
    month_table = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    User_Month_No = month_table[User_Month]
    Day_of_Week = dow.getDayOfTheWeek(User_Year, User_Month, User_Day)
    print(f'{User_Month_No}-{User_Day}-{User_Year} is a {Day_of_Week}')
    
makeCalendar()
getDayOfTheWeekForUserDate()