import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
print(myclient.list_database_names())
mydb = myclient["CSE"]
'''
mydblist=myclient.list_database_names()
if "CSE" in mydblist:
    print("Database exists")
else:
    print("Database doesnot exist")
'''
mycol = mydb['csea']
'''
mylist=mydb.list_collection_names()
if 'csea' in mylist:
    print("exists")
else :
    print("doesnot exist")
'''
mydict={"name":"chay","rollno":"228r1a0546"}
mydict={"name":"navya","rollno":"228r1a0546"}
mydict={"name":"deepu","rollno":"228r1a0546"}
mydict={"name":"anusha","rollno":"228r1a0546"}
#x = mycol.insert_one(mydict)
x = mycol.insert_many