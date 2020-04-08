# Problem 1 : Say "Hello, World!" With Python

print("Hello, World!)
_____________________________________________________________________________________________________________________________
# Problem 2 : Python If-Else
      
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
_____________________________________________________________________________________________________________________________
# Problem 3 : Arithmetic Operators
      
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
_____________________________________________________________________________________________________________________________
# Problem 4 : Python: Division
     
#Solution 1
a = 4
b = 3
print("{0}\n{1}".format(a//b, a/b))
_____________________________________________________________________________________________________________________________
# Problem 5 : Loops
      
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
_____________________________________________________________________________________________________________________________
# Problem 6 : Write a function

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
_____________________________________________________________________________________________________________________________
# Problem 7 : Print Function

#Solution 1
n = int(input())
print(*range(1, int(input())+1), sep='')
