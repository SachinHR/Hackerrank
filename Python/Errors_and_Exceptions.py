# Problem 1 : Exceptions

#Solution 1
for i in range(int(input())):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except BaseException as e:
        print("Error Code:",e)
____________________________________________________________________________________________________________________________________________
# Problem 2 : Incorrect Regex

#Solution 1
import re
for _ in range(int(input())):
    try:
        print(bool(re.compile(input())))
    except re.error:
        print("False")
