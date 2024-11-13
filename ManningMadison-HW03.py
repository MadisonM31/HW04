# Madison Manning
# UWYO COSC 1010
# 11/05/2024
# HW 03
# Lab Section: 10
# Sources, people worked with, help given to: 

months = {"01" : 31, "02" : 28, "03" : 31, "04" : 30, "05" : 31, "06" : 30, "07" : 31, "08" : 31,
        "09" : 30, "10" : 31, "11" : 30, "12" : 31}

week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def LeapYear(year):
    if year[-1] == 0 and year[-2] == 0:
        int(year)
        if year % 400 == 0:
            return True
        else:
            return False
    elif int(year) % 4 == 0:
        return True
    else:
        return False

def Jan1(year):
    year = int(year)
    y = year - 1
    j1 = (36 + y + (y/4) - (y/100) + (y/400))%7
    return j1

def valid_date(month, day, year):
    l_year = False
    if month == "02":
        l_year = LeapYear(year)
    if int(month) <= 12:
        for key in months.keys():
            if month == key:
                if month == "02" and l_year == True:
                    if int(day) <= months.get(key) + 1:
                        return True
                    else:
                        return False
                if int(day) <= months.get(key):
                    return True
                else:
                    return False
    else:
        return False   

while True:
    string = input("MM/DD/YYYY or exit to quit\n")
    if string.lower() == "exit":
        break
    string = string.split('/')
    day = string[1]
    month = string[0]
    year = string[2]
    day_count = 0
    if valid_date(month, day, year) == True:
        start_date = Jan1(year)
        for key in months.keys():
            if key == month:
                day_count += (int(day) -1)
                break
            else:
                day_count += months.get(key)
        if LeapYear(year) == True and int(month) > 2:
            day_count += 1
        day_count = (day_count + (start_date // 1) )% 7
        print(f"{string[0]}/{string[1]}/{string[2]} {week_days[int(day_count)]}")
    else:
        print(f"{string[0]}/{string[1]}/{string[2]} Invalid Date")


