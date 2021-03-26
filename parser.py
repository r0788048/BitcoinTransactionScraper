import pymongo as mongo
import requests
import time
import redis

def loaddb():
    has = [none] * len(r.keys)
    allebs = [none] * len(r.keys)
    temp = 0
    
    r = redis.Redis()
    for key in r.keys():
    	has[temp] = key
    	allebs[temp] = r.get(key)
    	temp = temp + 1

    tel = 0
    for x in range(0, len(allebs)):
        if(x%3 == 1):
            if (float(allebs[x].text[:-4]) > float(allebs[tel].text[:-4])):
                tel = x
    
    string = {"hash": has[int((tel-1)/3)].text, "time": allebs[tel-1].text, "am_btc": allebs[tel].text, "am_usd": allebs[tel+1].text}
    x =  col_transactions.insert_one(string)

client = mongo.MongoClient("mongodb://127.0.0.1:27017")

transactions_db = client["transactions"]
col_transactions = transactions_db["transactions"]

while True:
    loaddb()
    time.sleep(60)
