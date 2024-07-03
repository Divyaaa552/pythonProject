fp1=open("csea1.txt","r")
if fp1 :
    print("File is opened successfully")
content=fp1.readline()
print(content)
content=fp1.readline()
print(content)

content=fp1.readline()
print(content)

fp1.close()
