# Problem 1 : Arrays

#Solution 1
import numpy
def arrays(arr):
    return numpy.array(arr[::-1],float)
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
____________________________________________________________________________________________________________________________________________
# Problem 2 : Shape and Reshape

#Solution 1
import numpy as np
l = np.array(list(map(int,input().split())))
l.shape = (3,3)
print(l)

#Solution 2
import numpy as np
l = np.array(list(map(int,input().split())))
print(np.reshape(l,(3,3)))
____________________________________________________________________________________________________________________________________________
# Problem 3 : Transpose and Flatten

#Solution 1
import numpy as np
arr = np.array([input().strip().split() for _ in range(int(input().split()[0]))],int)
print(arr.transpose())
print(arr.flatten())
____________________________________________________________________________________________________________________________________________
# Problem 4 : Concatenate

#Solution 1
import numpy as np
n,m,p = map(int,input().split())
arr = np.array([input().strip().split() for _ in range(n)],int)
arr1 = np.array([input().strip().split() for _ in range(m)],int)
print(np.concatenate((arr,arr1)))
____________________________________________________________________________________________________________________________________________
# Problem 5 : Zeros and Ones

#Solution 1
import numpy
nums = tuple(map(int, input().split()))
print (numpy.zeros(nums, dtype = numpy.int))
print (numpy.ones(nums, dtype = numpy.int))
____________________________________________________________________________________________________________________________________________
# Problem 6 : Eye and Identity

#Solution 1
import numpy
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))
____________________________________________________________________________________________________________________________________________
# Problem 7 : Array Mathematics

#Solution 1
import numpy as np
n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype = int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep = "\n")
____________________________________________________________________________________________________________________________________________
# Problem 8 : Floor, Ceil and Rint

#Solution 1
import numpy as np
np.set_printoptions(sign=' ')
a = np.array(input().split(), float)
print(np.floor(a), np.ceil(a), np.rint(a),sep='\n')
____________________________________________________________________________________________________________________________________________
# Problem 9 : Sum and Prod

#Solution 1

print(np.prod(np.sum(a,axis = 0)))
____________________________________________________________________________________________________________________________________________
# Problem 10 : Min and Max

#Solution 1
import numpy as np
n,m = map(int,input().split())
a = np.array([input().split() for _ in range(n)],int)
print(np.max(np.min(a,axis = 1)))
____________________________________________________________________________________________________________________________________________
# Problem 11 : Mean, Var, and Std

#Solution 1
import numpy as np
np.set_printoptions(legacy='1.13')
n , m =map(int,input().split())
a = np.array([input().split() for _ in range(n)],int)
print(np.mean(a,axis=1), np.var(a, axis=0), np.std(a),sep='\n')
____________________________________________________________________________________________________________________________________________
# Problem 12 : Dot and Cross

#Solution 1
import numpy as np
n = int(input())
a = np.array([list(map(int,input().split())) for _ in range(n)],int)
b = np.array([list(map(int,input().split())) for _ in range(n)],int)
print(np.dot(a,b))
____________________________________________________________________________________________________________________________________________
# Problem 13 : Inner and Outer

#Solution 1
import numpy as np
a = np.array(input().split(),int)
b = np.array(input().split(),int)
print(np.inner(a,b))
print(np.outer(a,b))
____________________________________________________________________________________________________________________________________________
# Problem 14 : Polynomials

#Solution 1
import numpy as np
p,n = np.array(input().split(),float), int(input())
print(np.polyval(p,n))

#Solution 2
print(__import__('numpy').polyval(list(map(float,input().split())),float(input())))
____________________________________________________________________________________________________________________________________________
# Problem 14 : Linear Algebra

#Solution 1
import numpy as np
np.set_printoptions(legacy = '1.13')
a = np.array([input().split() for _ in range(int(input()))],float)
print(np.linalg.det(a))
