import pymongo as mongo
import requests
import time
import redis

def loaddb():
    r = redis.Redis()
    	
    has = []
    allebs = []
    
    for key in r.keys():
    	has.append(key)
    	
    	string = r.get(key)
    	arr = string.decode().split(" | ")
    	for val in arr:
    	    allebs.append(val)

    tel = 0
    for x in range(0, len(allebs)):
        if(x%3 == 1):
            if (float(allebs[x][:-4]) > float(allebs[tel][:-4])):
                tel = x
    print("parsed")
    string = {"hash": has[int((tel-1)/3)], "time": allebs[tel-1], "am_btc": allebs[tel][:-4], "am_usd": allebs[tel+1]}
    x =  col_transactions.insert_one(string)

client = mongo.MongoClient("mongodb://127.0.0.1:27017")
db_transactions = client["BitCoinTransaction"]
col_transactions = db_transactions["BitCoinTransaction"]
