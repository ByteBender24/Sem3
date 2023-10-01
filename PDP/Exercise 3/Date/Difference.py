'''
Difference Module
• DifferenceWithCurrent(Date)
• Difference(Date1,Date2)
• DaysAfter(#days)
• DaysBefore(#days)
• MonthAfter(#Months)
• MonthBefore(#Month)

Author : Harishraj S
Date : 27-09-2023
'''

from datetime import datetime, timedelta

def difference_with_current(date):
    now = datetime.now().date()
    date_obj = date
    if isinstance(date, str):
        date_obj = datetime.strptime(date, "%d.%m.%Y")
    delta = date_obj - now
    return delta.days

def difference(date1, date2):
    date1_obj, date2_obj = date1, date2
    if isinstance(date1, str):
        date1_obj = datetime.strptime(date1, "%d.%m.%Y")
    if isinstance(date2, str):
        date2_obj = datetime.strptime(date2, "%d.%m.%Y")
    delta = date1_obj - date2_obj
    return delta.days

def days_after(days):
    now = datetime.now()
    future_date = now + timedelta(days=days)
    return future_date.strftime("%d.%m.%Y")

def days_before(days):
    now = datetime.now()
    past_date = now - timedelta(days=days)
    return past_date.strftime("%d.%m.%Y")

def month_after(months):
    now = datetime.now()
    future_date = now + timedelta(days=30 * months)
    return future_date.strftime("%d.%m.%Y")

def month_before(months):
    now = datetime.now()
    past_date = now - timedelta(days=30 * months)
    return past_date.strftime("%d.%m.%Y")



if __name__ == "__main__":
    
    print (difference_with_current('24.12.2004'))

    # Test the difference_with_current function
    current_date = datetime.now().strftime("%d.%m.%Y")
    test_date = "24.12.2004"
    days_difference = difference_with_current(test_date)
    print(f"Days between {test_date} and current date {current_date}: {days_difference} days")

    # Test the difference function
    date1 = "01.01.2000"
    date2 = "31.12.2000"
    days_difference = difference(date1, date2)
    print(f"Days between {date1} and {date2}: {days_difference} days")

    # Test the days_after function
    days = 10
    future_date = days_after(days)
    print(f"{days} days after current date: {future_date}")

    # Test the days_before function
    days = 5
    past_date = days_before(days)
    print(f"{days} days before current date: {past_date}")

    # Test the month_after function
    months = 2
    future_date = month_after(months)
    print(f"{months} months after current date: {future_date}")

    # Test the month_before function
    months = 3
    past_date = month_before(months)
    print(f"{months} months before current date: {past_date}")
