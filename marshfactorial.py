import marshal
src = '''
def fact(n) :
     if n == 0 or n == 1 :
          print(1)
     else : 
          fact = fact(n) * fact(n-1)
n = 5
print(fact(5))
'''
code = compile(src,"src","exec")
fp = open("m.txt","wb")
marshal.dump(code,fp)
fp.close()
