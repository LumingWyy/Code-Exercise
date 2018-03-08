'''
Created on 2017/07/05
@author: Wang Luming
'''
def IsPrime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        m = 3
        while m * m <= n and n % m != 0:
            m = m + 2
        if m * m <= n:
            return False
        else:
            return True
            
n = int(raw_input('Enter a positive integer '))
if IsPrime(n):
    print n
else:
    for j in range(int(n / 2) + 1):
        for i in range(2, n):
            t = n % i
            if t == 0:
                print i
                n = n // i
