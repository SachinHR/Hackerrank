# Problem 1 : collections.Counter()

#Solution 1
X, N = int(input()), input().split()
total = 0
for _ in range(int(input())):
    a = 0
    s,a = input().split()
    if s in N:
        total += int(a)
        del N[N.index(s)]
print(total)

#Solution 2
from collections import Counter
X, N = int(input()), Counter(map(int,input().split()))
total = 0
for _ in range(int(input())):
    s,a = map(int,input().split())
    if N[s]:
        total += a
        N[s] -= 1
print(total)
____________________________________________________________________________________________________________________________________________
# Problem 2 : DefaultDict Tutorial

#Solution 1
from collections import defaultdict
d = defaultdict(list)
list1 = []
n,m = map(int,input().split())
for i in range(n):
    d[input()].append(i+1)
for i in range(m):
    list1 = list1 + [input()]
for i in list1:
    if i in d:
        print(" ".join(map(str,d[i])))
    else:
        print(-1)
____________________________________________________________________________________________________________________________________________
# Problem 3 : Collections.namedtuple()

#Solution 1
from collections import namedtuple
n, columns = int(input()), input().split()
Grade = namedtuple("Grade", columns)
marks = [int(Grade._make(input().split()).MARKS) for _ in range(n)]
print(sum(marks)/len(marks))

#Solution 2
students, marks = int(input()), input().split().index("MARKS")
print(sum([int(input().split()[marks]) for _ in range(students)]) / students)
____________________________________________________________________________________________________________________________________________
# Problem 4 : Collections.OrderedDict()

#Solution 1
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    i,s,v = input().rpartition(" ")
    d[i] = d.get(i,0) + int(v)
for i,q in d.items():
    print(i,q)
____________________________________________________________________________________________________________________________________________
# Problem 5 : Collections.deque()

#Solution 1
from collections import deque
d = deque()
for _ in range(int(input())):
    cmd,*a = input().split()
    if a:
        eval("d." + cmd + "(" + a.pop() + ")")
    else:
        eval("d." + cmd + "()")
print(" ".join(map(str,d)))

#Solution 2
from collections import deque
d = deque()
for _ in range(int(input())):
    inp = input().split()
    getattr(d, inp[0])(*inp[1] if len(inp) > 1 else [])
print(*[item for item in d])
____________________________________________________________________________________________________________________________________________
# Problem 6 : Company Logo

#Solution 1
from collections import Counter
[print(*c) for c in Counter(sorted(input())).most_common(3)]
____________________________________________________________________________________________________________________________________________
# Problem 7 : Word Order

#Solution 1
from collections import Counter
d = Counter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())
____________________________________________________________________________________________________________________________________________
# Problem 8 : Pilling Up!

#Solution 1
from collections import deque
for _ in range(int(input())):
    n = int(input())
    s = deque(map(int,input().split()))
    r = "Yes"
    if max(s) not in (s[0],s[-1]):
        r = "No"
    print(r)
