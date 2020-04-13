# Problem 1 : Zipped!

#Solution 1
n,x = map(int,input().split())
print(*[sum(i)/len(i) for i in zip(*[map(float,input().split()) for _ in range(x)])],sep="\n")
____________________________________________________________________________________________________________________________________________
# Problem 2 : Input()

#Solution 1
x,k = map(int,input().split())
print(eval(input()) == k)
____________________________________________________________________________________________________________________________________________
# Problem 3 : Python Evaluation

#Solution 1
eval(input())
____________________________________________________________________________________________________________________________________________
# Problem 4 : Any or All

#Solution 1
N, n = input(), input().split()
print(all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n]))
____________________________________________________________________________________________________________________________________________
# Problem 5 : Athlete Sort

#Solution 1
n,m = map(int,input().split())
rows = [input() for _ in range(n)]
k = int(input())
print(*[row for row in sorted(rows, key = lambda row:int(row.split()[k]))],sep="\n")
____________________________________________________________________________________________________________________________________________
# Problem 6 : ginortS

#Solution 1
print(*sorted(input(),key=lambda c:(c.isdigit() - c.islower(), c in "02468",c)),sep="")
