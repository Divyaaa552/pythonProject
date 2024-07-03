import marshal
fp = open("m.txt","rb")
data = marshal.load(fp)
exec(data)