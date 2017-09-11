'''
Created on 2017/07/05
@author: Wang Luming
'''
def checkdate(year, month, date):
    import datetime
    y = year
    m = month
    d = date
    try:
        datetime.date(y, m, d)
        return True
    except:
        return False
while 1:
    date = int(raw_input('Enter a date'))
    month = int(raw_input('Enter a month'))
    year = int(raw_input('Enter a year'))

    if checkdate(year, month, date):
        if (year < 1868) or (year == 1868 and month < 9) or (year == 1868 and month == 9 and date < 8):
            print 'Time is expected later than 1868,9,8.'
            break
        elif (year == 1868 and month > 9) or (year == 1868 and month == 9 and date >= 8):
            print u'\u660e\u6cbb\u5143\u5e74'
            break
        elif (year < 1912) or (year == 1912 and month < 7) or (year == 1912 and month == 7 and date < 30):
            print u'\u660e\u6cbb', year - 1867, u'\u5e74'
            break
        elif (year == 1912 and month > 7) or (year == 1912 and month == 7 and date >= 30):
            print u'\u5927\u6b63\u5143\u5e74'
            break
        elif (year < 1926) or (year == 1926 and month < 12) or (year == 1912 and month == 12 and date < 25):
            print u'\u5927\u6b63', year - 1911, u'\u5e74'
            break
        elif (year == 1926 and month == 12) or (year == 1926 and month == 12 and date >= 25):
            print u'\u662d\u548c\u5143\u5e74'
            break
        elif (year < 1989) or (year == 1912 and month == 1 and date < 7):
            print u'\u662d\u548c', year - 1925, u'\u5e74'
            break
        elif (year == 1989 and month > 1) or (year == 1989 and month == 1 and date >= 7):
            print u'\u5e73\u6210\u5143\u5e74'
            break
        else:
            print u'\u5e73\u6210', year - 1988, u'\u5e74'
            break
    else:
        print'Please enter the correct date format.'

