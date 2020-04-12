# Problem 1 : itertools.product()

#Solution 1
from itertools import product
print(*list(product(list(map(int,input().split())), list(map(int,input().split())))))
____________________________________________________________________________________________________________________________________________
# Problem 2 : itertools.permutations()

#Solution 1
from itertools import permutations
a,n = input().split()
print(*["".join(i) for i in permutations(sorted(a),int(n))],sep = "\n")
____________________________________________________________________________________________________________________________________________
# Problem 3 : itertools.combinations()

#Solution 1
from itertools import combinations
a,n = input().split()
for i in range(1, int(n)+1):
    print(*["".join(i) for i in combinations(sorted(a),i)],sep = "\n")
____________________________________________________________________________________________________________________________________________
# Problem 4 : itertools.combinations_with_replacement()

#Solution 1
from itertools import combinations_with_replacement
a,n = input().split()
print(*["".join(i) for i in combinations_with_replacement(sorted(a),int(n))],sep = "\n")
____________________________________________________________________________________________________________________________________________
# Problem 5 : Compress the String!

#Solution 1
from itertools import groupby
print(*[(len(list(c)), int(k)) for k,c in groupby(input())])
____________________________________________________________________________________________________________________________________________
# Problem 6 : Iterables and Iterators

#Solution 1
from itertools import combinations
n, l, k = int(input()), input().split(), int(input())
C = list(combinations(l,k))
F = filter(lambda c: "a" in c, C)
print("{0:.4}".format(len(list(F))/len(C)))
____________________________________________________________________________________________________________________________________________
# Problem 7 : Maximize It!

#Solution 1
from itertools import product
K, M = map(int, input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))
