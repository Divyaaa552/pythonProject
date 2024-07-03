"""
list_ = []
n = int(input())
for i in range(n):
    ele = int(input())
    list_.append(ele)
print(list_)
"""
def commas(str) :
    x=str.replace('',',')[1:-1]
    return x
print(repr(commas("Apple")))

def removeword(str,word) :
    y = str.replace(word,' ')
    return y

str = "hello good morning hi hello good"
word = "hello"
print(removeword(str,word))

print(ord('A'))
print(ord('&'))
print(ord('*'))
print(ord('~'))
print(ord('!'))
print(chr(57))
print(chr(1))
print(chr(2))
print(chr(33))
print(chr(34))
print(chr(35))
print(chr(36))
str = "hello good morning"
ch = list(str)
print(ch)
print(ord('h'))
 def convert(str) :
     ch = list(str)
     for i in range(len(str))
         if i==0 and ch[i]!=' ' :
             if ch[i]>='a' and ch[i]<='z' :
                 ch[i]=chr(ord(ch[i]-ord('a')+ord('A')))
         str1="",ch[i]
     