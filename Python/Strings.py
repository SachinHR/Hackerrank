# Problem 1 : sWAP cASE

#Solution 1
a = "SaChIn"
print(a.swapcase())
_______________________________________________________________________________________________________________________________
# Problem 2 : String Split and Join

#Solution 1
a = "A B C"
a = a.split()
print("-".join(a))

#Solution 2
a = "A B C"
print("-".join(a.split()))

#Solution 3
a = "A B C"
print(a.replace(" ","-"))
_______________________________________________________________________________________________________________________________
# Problem 3 : What's Your Name?

#Solution 1
a = "Sachin"
b = "H R"
print("Hello "+ a + " " + b + "! You just delved into python.")
______________________________________________________________________________________________________________________________
# Problem 4 : Mutations

#Solution 1
string = "abracadabra"
print(string[:5] + "k" + string[6:])
__________________________________________________________________________________________________________________________________
# Problem 5 : Find a string

#Solution 1
string = "ABCDCDC"
substring = "CDC"
count = 0
for i in range((len(string) - len(substring)) + 1):
    if substring == string[i : i + 3]:
        count += 1
print(count)

#Solution 2
string, substring = (input().strip(), input().strip())
print(sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))
__________________________________________________________________________________________________________________________________
# Problem 6 : String Validators

#Solution 1
a = input()
print(any(i.isalnum() for i in a))
print(any(i.isalpha() for i in a))
print(any(i.isdigit() for i in a))
print(any(i.islower() for i in a))
print(any(i.isupper() for i in a))

#Solution 2
s = input()
for test in ["isalnum","isalpha","isdigit","islower","isupper"]:
    print(any(eval("c." + test + "()") for c in s))

#Solution 3
s = input()
for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    print(any(method(c) for c in s))
___________________________________________________________________________________________________________________________________
# Problem 7 : Text Alignment

#Solution 1
thickness = int(input())           #This must be an odd number
c = 'H'
for i in range(thickness):         #Top Cone
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
for i in range(thickness+1):       #Top Pillars
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
for i in range((thickness+1)//2):  #Middle Belt
    print((c*thickness*5).center(thickness*6))    
for i in range(thickness+1):       #Bottom Pillars
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
for i in range(thickness):         #Bottom Cone
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
_____________________________________________________________________________________________________________________________________
# Problem 8 : Text Wrap

#Solution 1
def wrap(string, max_width):
    return "\n".join([string[i : i + max_width] for i in range(0,len(string),max_width)])
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
______________________________________________________________________________________________________________________________________
# Problem 9 : Designer Door Mat

#Solution 1
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
_____________________________________________________________________________________________________________________________________
# Problem 10 : String Formatting

#Solution 1
n = int(input())
width = len("{0:b}".format(n))
for i in range(1,n+1):
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width = width))
______________________________________________________________________________________________________________________________________
# Problem 11 : Alphabet Rangoli

#Solution 1
import string
alpha = string.ascii_lowercase
n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1] + s[1:]).center(4*n-3, "-"))
print("\n".join(L[:0:-1] + L))
_______________________________________________________________________________________________________________________________________
# Problem 12 : Capitalize!

#Solution 1
s = input()
for x in s.split():
    s = s.replace(x, x.capitalize())
print(s)
_______________________________________________________________________________________________________________________________________
# Problem 13 : The Minion Game

#Solution 1
s = input()
vowel = 'AEIOU'
kevsc = 0
stuart = 0
for i in range(len(s)):
    if s[i] not in vowel:
        stuart += (len(s) - i)
    else:
        kevsc += (len(s) - i)
if kevsc > stuart:
    print("kevsc ",kevsc)
elif kevsc < stuart:
    print("Stuart ",stuart)
else:
    print("Draw")

#Solution 2
s = input()
vowel = "AEIOU"
l = len(s)
kevin = sum(len(s)-i for i in range(len(s)) if s[i] in vowel)
stuart = len(s)*(len(s) + 1)//2 - kevin
if kevin < stuart:
	print('Stuart ',stuart)
elif kevin > stuart:
	print('Kevin ',kevin)
else:
	print("Draw")
_______________________________________________________________________________________________________________________________________
# Problem 14 : Merge the Tools!

#Solution 1
S = input()
k = int(input())
l = []
t = [S[(k * i) : k + (k * i)] for i in range(len(S)//k)]
for part in t:
    d = {}
    print("".join([d.setdefault(c,c) for c in part if c not in d]))

#Solution 2
s = input()
n = int(input())
for part in zip(*([iter(s)] * n)):
    d = dict()
    print("".join([d.setdefault(c,c) for c in part if c not in d]))
