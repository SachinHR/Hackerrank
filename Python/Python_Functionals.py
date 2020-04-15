# Problem 1 : Map and Lambda Function

#Solution 1
cube = lambda x:pow(x,3)
def fib(n):
    l = [0,1]
    for i in range(2,n):
        l.append(l[i-2] + l[i-1])
    return l[0:n]
print(list(map(cube,fib(int(input())))))
____________________________________________________________________________________________________________________________________________
# Problem 2 : Validating Email Addresses With a Filter

#Solution 1
def fun(s):
    s_prcocess = s.replace('@','.').split('.')
    order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468-_'
    if len(s_prcocess) == 3 and all(s_items != '' for s_items in s_prcocess):
        if (len(s_prcocess[2]) <= 3 and s_prcocess[1].isalnum() and all(item in order for item in s_prcocess[0])):
            return True
    return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
____________________________________________________________________________________________________________________________________________
# Problem 3 : Reduce Function

#Solution 1
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y : x * y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
