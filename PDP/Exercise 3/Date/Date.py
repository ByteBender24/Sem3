'''
Date Module
• Create and display dates

Author : Harishraj S
Date : 27-09-2023
'''

import datetime

class Date:

    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date
    
    def __str__ (self):
        return f"{self.year}/{self.month}/{self.date}"
    
    def showdate(self):
        return f"{self.year}/{self.month}/{self.date}"
    
    def gatedate(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date


def date_obj_converter(string, format):
    '''
    Be sure to give the format correctly, consistent with string given \n
    if string = '24/3/2004' give format ='%d/%m/%Y' \n            
    if string = '24-3-2004' give format ='%d-%m-%Y'
    '''
    date_obj = datetime.datetime.strptime(string, format).date()
    return date_obj
    
if __name__ == "__main__": 
    
    now_datetime = datetime.datetime.now()
    now_date = datetime.date.today()

    print (now_date)
    print (now_datetime)

    date1 = Date(2004, 3, 24)
    print(date1)

    date_obj = date_obj_converter(date1.showdate(), '%Y/%m/%d')
    print (date_obj)

    help(date_obj_converter)