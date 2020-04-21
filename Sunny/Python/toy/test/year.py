def isLeapYear(year) : 
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

def lastDay(year, month) :
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year) :
        m[1] = 29
    return m[month - 1]

def totalYear(year, month, day) :
    total = 0
    for i in range(year-1) :
        if isLeapYear(i) :
            total += 366
        else :
            total += 365
    for i in range(month - 1) :
        total += lastDay(year, i+1)
    total += day - 1
    return total

def weekDay(year, month, day) :
    return totalYear(year, month, day) % 7



year, month, day = map(int,input('년 월 일 을 입력하세요 : ').split())


print('='*28)
print('        {}년 {}월'.format(year,month))
print('='*28)
print(' 일  월  화  수  목  금  토 ')
print('='*28)


print('    ' * weekDay(year, month, 1), end = '')
for i in range(1, lastDay(year,month)+1) :
    print(' %2d' % i, end=' ')
    if (weekDay(year, month, 1) + i) % 7 == 0 :
        print()
if (weekDay(year, month, 1) + i) % 7 == 0 :
    print('='*28)
else :
    print('\n' + '='*28)
