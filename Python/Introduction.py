#Problem 1

print("Hello, World!)

#Problem 2

#Solution 1
N = int(input())
if (N % 2 != 0):
    print("Weird")
else:
    if(2 <= N <= 5):
        print("Not Weird")
    elif(6 <= N <= 20):
        print("Weird")
    elif(N >= 20):
        print("Not Weird")

#Solution 2
N = int(input())
check = { True : "Not Weird", False : "Weird" }
print(check[ N%2 == 0 and ((N in range(2,5)) or (N > 20)) ])

#Problem 3

#Solution 1
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)

#Solution 2
a = int(input())
b = int(input())
print("{0} \n{1} \n{2}".format(a+b, a-b, a*b))

#Problem 4

#Solution 1
n = int(input())
for i in range(n):
    print(i * i)
    
#Solution 2
n = int(input())
print(*[num**2 for num in range(n)], sep='\n')

#Solution 3
n = int(input())
[print(num**2) for num in range(n)]

#Problem 5

#Solution 1
n = int(input())
[print(num**2,end="") for num in range(n)]

#Solution 2
n = int(input())
print(*[num**2 for num in range(n)], sep = "")
#or
print(*range(1, int(input())+1), sep='')

#Problem 6

#Solution 1
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
        return True
    else:
        return False
year = int(input())
print(is_leap(year))

#Solution 2
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
year = int(input())
print(is_leap(year))

#Problem 7

#Solution 1
x,y,z,n = (int(input()) for i in range(4))
print([[a, b, c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if (a + b + z != n)])
