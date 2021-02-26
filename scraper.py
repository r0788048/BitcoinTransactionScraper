from bs4 import BeautifulSoup
import pymongo as mongo
import requests
import time

def scrape():
    url = 'https://www.blockchain.com/btc/unconfirmed-transactions'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    #print(soup.prettify())

    has = soup.find_all('a',{ "class" : "sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK"})
    allebs = soup.find_all('span',{ "class" : "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"})

    tel = 0
    for x in range(0, len(allebs)):
        if(x%3 == 1):
            if (float(allebs[x].text[:-4]) > float(allebs[tel].text[:-4])):
                tel = x
    
    string = {"hash": has[(tel-1)%3].text, "time": allebs[tel-1].text, "am_btc": allebs[tel].text, "am_usd": allebs[tel+1].text}
    x =  col_transactions.insert_one(string)

client = mongo.MongoClient("mongodb://127.0.0.1:27017")

transactions_db = client["transactions"]
col_transactions = transactions_db["transactions"]

while True:
    scrape()
    time.sleep(60)
