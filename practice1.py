'''
Created on 2017/07/05
@author: Wang Luming
'''
while 1:
    a = int(raw_input('enter the number `a` that the left point of the closed interval `ab`'))
    b = int(raw_input('enter the number `b` that the right point of the closed interval `ab`'))
    c = int(raw_input('enter the number `c` that the left point of the closed interval `cd`'))
    d = int(raw_input('enter the number `d` that the right point of the closed interval `cd`'))
    if a < b and c < d:
        if b < c or d < a:
            print 'The interval `ab`[', a, ',', b, '] doesn`t overlap with `cd`[', c, ',', d, ']'
        elif (c >= a and c <= b) or (d >= a and d <= b) or (a >= c and a <= d) or (b >= c and b <= d):
            print 'The interval `ab`[', a, ',', b, '] overlap with `cd`[', c, ',', d, ']'
        break
    else:
        print '`b` should be bigger than `a` or `d` should be bigger than `c`'
