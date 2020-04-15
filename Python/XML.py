# Problem 1 : XML 1 - Find the Score

#Solution 1
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    score = len(node.attrib)
    for element in node.findall('.//*'):
        score += len(element.attrib)
    return score
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print get_attr_number(root)
____________________________________________________________________________________________________________________________________________
# Problem 2 : XML2 - Find the Maximum Depth

#Solution 1
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if (level == maxdepth):
        maxdepth += 1
    for child in elem:
        depth(child, level + 1)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
