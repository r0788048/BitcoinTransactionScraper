import pymongo as mongo
import requests
import time
import redis

def loaddb():
    has = [none] * len(r.keys)
    allebs = [none] * len(r.keys)
    temph = 0
    tempa = 0
    
    r = redis.Redis()
    for key in r.keys():
    	has[temph] = key
    	temph = temph + 1
    	
    	string = r.get(key)
    	arr = string.split(" | ")
    	for val in arr:
    	    allebs[tempa] = val
    	    tempa = tempa + 1

    tel = 0
    for x in range(0, len(allebs)):
        if(x%3 == 1):
            if (float(allebs[x].text[:-4]) > float(allebs[tel].text[:-4])):
                tel = x
    print("parsed")
    string = {"hash": has[int((tel-1)/3)].text, "time": allebs[tel-1].text, "am_btc": allebs[tel].text, "am_usd": allebs[tel+1].text}
    x =  col_transactions.insert_one(string)

while True:
    loaddb()
    time.sleep(60)
