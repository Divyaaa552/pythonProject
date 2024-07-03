import math
p = float(input("Enter principal amount:"))
t = int(input("Enter time:"))
r = float(input("Enter rate of interest:"))
n = int(input("Enter the value of n:"))
a = p * pow((1 + r/n),n*t)
ci = a-p
print(ci)