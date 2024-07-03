import dbm
db = dbm.open("dbm1.db","n")
#with dbm.open("dbm1.db") as db :
db['one']='1'
db['two']='2'
db['three']='3'
