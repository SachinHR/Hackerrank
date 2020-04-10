# Problem 1 : Introduction to Sets

#Solution 1
n = int(input())
array = list(map(int,input().split()))
sum(set(array))/len(set(array))
_______________________________________________________________________________________________________________________________________
# Problem 2 : Symmetric Difference

#Solution 1
a,b = [set(input().split()) for _ in range(4)][1::2]
print('\n'.join(sorted(a.symmetric_difference(b), key=int)))
_______________________________________________________________________________________________________________________________________
# Problem 3 : Set.add()

#Solution 1
print(len(set([input() for _ in range(int(input()))])))
_______________________________________________________________________________________________________________________________________
# Problem 4 : Set .discard(), .remove() & .pop()

#Solution 1
n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+[""]))
print(sum(s))
_______________________________________________________________________________________________________________________________________
# Problem 5 : Set .union() Operation

#Solution 1
a,b = [set(input().split()) for _ in range(4)][1::2]
print(len(a.union(b)))
