from calendar import *
import datetime
'''year = int(input('enter year : '))
monday = 0
for month in range(1,13):
    dt = datetime.date(year,month,1)

    if dt.weekday()==0:
        monday += 2
        print(month)

print('Number of months starting with Monday =', monday)        '''

# 
'''str_date = input('enter the date in dd-mm-yyyy ')

d, m, y = str_date.split('-')
d1= datetime.date(int(y),int( m),int(d))
print('Date' , d1)'''

# 
from datetime import *

'''def age(dob):
    today = date.today()
    years = today.year - dob.year

    if (today.month , today.day) < (dob.month ,dob.day):
        years -= 1

    return years

print(age(date(2000,2,10)))    '''

# 
import datetime as dt
def prev_day(day):
    week_days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

    today = dt.date.today()
    t_dw= today.weekday()
    dw= week_days.index(day)

    diff = dw - t_dw
    if diff < 0:
        new_date= today + dt.timedelta(diff)
    else:
        new_date=today + dt.timedelta(-(7-diff))

    return new_date

print('today:',dt.date.today())
print('prev:', prev_day('monday'))



# 