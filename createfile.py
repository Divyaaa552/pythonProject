"""
open()
read()
readline()
write()
writeline()
close()
seek()
tell()
"""
fp =open("csea1.txt","w")
if fp :
    print("File is created successfully")
fp.write("Hey People!!\n Let's make the world a better place to live in.\nThe world is full of opportunities,Let us chase them!")

fp.close()
