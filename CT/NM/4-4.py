# 모순된 경우는 없다.

m1,d1,m2,d2 = map(int,input().split())

weekdays = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

def cal_days(m,d):
    weekdays = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    days = 0
    for i in range(1,m):
        days += weekdays[i]
    days += d
    return days

result_days = cal_days(m2,d2)-cal_days(m1,d1)
while result_days<0:
    result_days+=7
print(weekdays[result_days%7])

