# Problem 1 : Detect Floating Point Number

#Solution 1
import re
for _ in range(int(input())):
    print(bool(re.match(r"^[-+]?[0-9]*\.[0-9]+$",input())))
____________________________________________________________________________________________________________________________________________
# Problem 2 : Re.split()

#Solution 1
regex_pattern = r"[,.]"
import re
print("\n".join(re.split(regex_pattern, input())))
____________________________________________________________________________________________________________________________________________
# Problem 3 : Group(), Groups() & Groupdict()

#Solution 1
import re
m = re.search(r"([a-zA-Z0-9])\1+",input().strip())
print(m)
print(m.group(1) if m else -1)

#Solution 2
import re
m = re.search(r'([^\W_])\1+',input())
print(m.group(1) if m else -1)
____________________________________________________________________________________________________________________________________________
# Problem 4 : Re.findall() & Re.finditer()

#Solution 1
import re
m = re.findall("(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})" + "[qwrtypsdfghjklzxcvbnm]", input(), re.I)
print("\n".join(m or ["-1"]))
____________________________________________________________________________________________________________________________________________
# Problem 5 : Re.start() & Re.end()

#Solution 1
import re

s = input()
k = input()
if k in s:
    print(*[(i.start(), (i.start()+len(k)-1)) for i in re.finditer(r"(?={})".format(k),s)],sep="\n")
else:
    print('(-1, -1)')
____________________________________________________________________________________________________________________________________________
# Problem 6 : Validating Roman Numerals

#Solution 1
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))
____________________________________________________________________________________________________________________________________________
# Problem 7 : Validating phone numbers

#Solution 1
import re
[print('YES' if re.match(r'[789]\d{9}$',input()) else 'NO') for _ in range(int(input()))] 
____________________________________________________________________________________________________________________________________________
# Problem 8 : Validating and Parsing Email Addresses

#Solution 1
import re
for _ in range(int(input())):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)
____________________________________________________________________________________________________________________________________________
# Problem 9 : Hex Color Code

#Solution 1
import re
for i in range(int(input())):
    s=input()
    x=s.split()
    if len(x)>1  and  '{' not in x:
        x=re.findall(r'#[a-fA-F0-9]{3,6}',s)
        [print(i) for  i in x]
____________________________________________________________________________________________________________________________________________
# Problem 10 : HTML Parser - Part 1

#Solution 1
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        for attr in attrs:
                print ('->',' > '.join(map(str, attr)))
    def handle_endtag(self, tag):
        print('End   :', tag)
    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for attr in attrs:
                print('->',' > '.join(map(str,attr)))

html = ""
for i in range(int(input())):
    html += input()


parser = MyHTMLParser()
parser.feed(html)
parser.close()
____________________________________________________________________________________________________________________________________________
# Problem 11 : HTML Parser - Part 2

#Solution 1

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data != '\n':
            if '\n' not in data:
                print(">>> Single-line Comment")
                print(data)
            else:
                print(">>> Multi-line Comment")
                print(data)
            
    def handle_data(self, data):
        if data != '\n': 
            print(">>> Data")
            print(data)
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
____________________________________________________________________________________________________________________________________________
# Problem 12 : Detect HTML Tags, Attributes and Attribute Values

#Solution 1
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print("->", attr, ">", value)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print("->", attr, ">", value)

html = ''
for _ in range(int(input())):
    html += input().rstrip() + '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
____________________________________________________________________________________________________________________________________________
# Problem 13 : Validating UID

#Solution 1
import re
for _ in range(int(input())):
    N = input()
    if N.isalnum() and len(N) == 10:
        if bool(re.search(r'(.*[A-Z]){2,}',N)) and bool(re.search(r'(.*[0-9]){3,}',N)):
            if re.search(r'.*(.).*\1+.*',N):
                print("Invalid")
            else:
                print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
____________________________________________________________________________________________________________________________________________
# Problem 14 : Regex Substitution

#Solution 1
import re
for i in range(int(input())):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))
____________________________________________________________________________________________________________________________________________
# Problem 15 : Validating Credit Card Numbers

#Solution 1
import re
TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for _ in range(int(input().strip())):
    print("Valid" if TESTER.search(input().strip()) else "Invalid")
____________________________________________________________________________________________________________________________________________
# Problem 16 : Validating Postal Codes

#Solution 1
regex_integer_in_range = r"^[1-9][\d]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"
import re
P = input()
print (bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
____________________________________________________________________________________________________________________________________________
# Problem 17 : Matrix Script

#Solution 1
import re

n, m = map(int, input().split())
a, b = [], ""
for _ in range(n):
    a.append(input())
for z in zip(*a):
    b += "".join(z)
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))
