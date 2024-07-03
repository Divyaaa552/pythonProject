import shelve
#sh = shelve.open("shelve1")
with shelve.open("shelve1") as sh :
    sh['one']=1
    sh['two']=2
    sh['three'] = 3
    sh.close()