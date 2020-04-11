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
_______________________________________________________________________________________________________________________________________
# Problem 6 : Set .intersection() Operation

#Solution 1
a,b = [set(input().split()) for _ in range(4)][1::2]
print(len(a.intersection(b)))
_______________________________________________________________________________________________________________________________________
# Problem 7 : Set .difference() Operation

#Solution 1
a,b = [set(input().split()) for _ in range(4)][1::2]
print(len(a.difference(b)))
_______________________________________________________________________________________________________________________________________
# Problem 8 : Set .symmetric_difference() Operation

#Solution 1
a,b = [set(input().split()) for _ in range(4)][1::2]
print(len(a.symmetric_difference(b)))
_______________________________________________________________________________________________________________________________________
# Problem 9 : Set Mutations

#Solution 1
n,a = [set(input().split()) for _ in range(2)]
for _ in range(int(input())):
    cmd, *args = input().split()
    getattr(a,cmd)(set(input().split()))
print(sum(map(int,a)))
_______________________________________________________________________________________________________________________________________
# Problem 10 : The Captain's Room

#Solution 1
k,arr = int(input()),list(map(int,input().split()))
print(((sum(set(arr))*k)- (sum(arr)))//(k-1))
_______________________________________________________________________________________________________________________________________
# Problem 11 : Check Subset

#Solution 1
for _ in range(int(input())):
    x,a,y,b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))
_______________________________________________________________________________________________________________________________________
# Problem 12 : Check Strict Superset

#Solution 1
a = set(input().split())
is_strict_superset = []
for i in range(int(input())):
     is_strict_superset.append(a.issuperset(set(input().split(' '))))
print(all(is_strict_superset))
_______________________________________________________________________________________________________________________________________
# Problem 13 : No Idea!

#Solution 1
n,m = input().split()
s, a, b = input().split(), set(input().split()), set(input().split())
print(sum([(i in a) - (i in b) for i in s]))
