# Problem 1 : List Comprehensions

#Solution 1
x,y,z,n = (int(input()) for i in range(4))
print([[a, b, c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if (a + b + z != n)])
____________________________________________________________________________________________________________________________
# Problem 2 : Find the Runner-Up Score!

#Solution 1
n = int(input())
a = list(map(int,input().split()))
a = list(set(a))[1]
del a[a.index(max(a))]
print(max(a))

#Solution 2
n = int(input())
a = list(map(int,input().split()))
m = max(a)
while max(a) == m:
    a.remove(max(a))
print(max(a))
_____________________________________________________________________________________________________________________________
# Problem 3 : Nested Lists

#Solution 1
n = int(input())
arr = [[input(),float(input())] for _ in range(n)]
second_highest = sorted(list(set([marks for name, marks in arr])))[1]
print('\n'.join([a for a,b in sorted(arr) if b == second_highest]))
_____________________________________________________________________________________________________________________________
# Problem 4 : Finding the percentage

#Solution 1
N = int(input())
d = {}
for _ in range(N):
    r = input().split()
    d[r[0]] = list(map(float,r[1:]))
n = input()
print("{0:.2f}".format(sum(d[n])/len(d[n])))
_____________________________________________________________________________________________________________________________
# Problem 5 : Lists

#Solution 1
n = int(input())
l = []
for _ in range(n):
    i = input().split()
    c = i[0]
    il = list(map(int,i[1:]))
    if c == "insert":
        l.insert(il[0],il[1])
    elif c == "print":
        print(l)
    elif c == "remove":
        l.remove(il[0])
    elif c == "append":
        l.append(il[0])
    elif c == "sort":
        l.sort()
    elif c == "pop":
        l.pop()
    elif c == "reverse":
        l.reverse()
    else:
        continue
        
#Solution 2
n = int(input())
l = []
for _ in range(n):
    a = input().split()
    cmd = a[0]
    arg = a[1:]
    if cmd != "print":
        cmd += "(" + ",".join(arg) + ")"
        eval("l."+cmd)
    else:
        print(l)
_____________________________________________________________________________________________________________________________
# Problem 6 : [Tuples](https://www.hackerrank.com/challenges/python-tuples/problem)

#Solution 1
n = int(input())
a = tuple(map(int,input().split()))
print(hash(a))
