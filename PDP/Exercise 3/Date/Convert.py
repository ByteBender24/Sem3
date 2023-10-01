'''
Convert Module has the following operations.
• Convert_hrs_days(#hours)
• Convert_days_hours(#days)
• Convert_man_hrs_days(#hours)

Author : Harishraj S
Date : 27-09-2023
'''

def convert_hrs_days(hours):
    if hours >= 24 :
        days = hours/24
        return round (days, 2)
    return f"It is less than a day, {round (hours/24,2)} of a day is given"

def convert_days_hours(days):
    return days * 24

def convert_man_hrs_days(hours):
    if hours >= 8 :
        days = hours/8
        return round (days, 2)
    return f"It is less than a man hour day,\n{round (hours/8,2)} of a man hour day is given" 

def convert_days_years(days):
    return days // 365

if __name__ == "__main__":
    print (convert_days_hours(3))
    print (convert_hrs_days(30))
    print (convert_hrs_days(8))
    print (convert_hrs_days(48))
    print (convert_man_hrs_days(16))
    print (convert_man_hrs_days(30))
    print (convert_man_hrs_days(4))
