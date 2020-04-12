# Problem 1 : Polar Coordinates

#Solution 1
import cmath
print(*cmath.polar(complex(input())), sep = "\n")
____________________________________________________________________________________________________________________________________________
# Problem 2 : Mod Dic

#Solution 1
print("{0}\n{1}\n({0}, {1})".format(*divmod(int(input()), int(input()))))
____________________________________________________________________________________________________________________________________________
# Problem 3 : Mod Power

#Solution 1
a,b,m = int(input()), int(input()), int(input())
print(pow(a,b),pow(a,b,m),sep="\n")
____________________________________________________________________________________________________________________________________________
# Problem 4 : Integers Come In All Sizes

#Solution 1
print(pow(int(input()), int(input())) + pow(int(input()), int(input())))

#Solution 2
a,b,c,d = (int(input()) for _ in range(4))
print(pow(a,b) + pow(c,d))
____________________________________________________________________________________________________________________________________________
# Problem 5 : Find Angle MBC

#Solution 1
import math
AB,BC = int(input()), int(input())
print(str(int(math.degrees(math.atan2(AB,BC)))) + '\N{DEGREE SIGN}')
____________________________________________________________________________________________________________________________________________
# Problem 6 : Triangle Quest

#Solution 1
for i in range(1,int(input())):
    print((1111111111%(10 ** i)) * i)
____________________________________________________________________________________________________________________________________________
# Problem 7 : Triangle Quest 2

#Solution 1
for i in range(1,int(input())+1):
    print([0,1, 121, 12321, 1234321, 123454321, 12345654321, 1234567654321, 123456787654321, 12345678987654321, 12345678910987654321][i])
