a = {1,2,3,4,5,6}
b = {5,6,7,8,9}
print(a)
print(b)
c = a.union(b)
print("UNION:",c)
d = a.intersection(b)
print("INTERSECTION:",d)
e = a.difference(b)
print("a-b :",e)
f = b.difference(a)
print("b-a :",f)
if 9 not in a :
    print("Hi!!!")
else :
    print("Hello!!")
