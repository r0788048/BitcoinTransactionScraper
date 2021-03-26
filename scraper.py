from bs4 import BeautifulSoup
import requests
import time
import redis

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
            redisstring =  allebs[x-1].text + ' | ' + allebs[x].text + ' | ' + allebs[x+1].text
            r = redis.Redis()
            r.set(has[int((x-1)/3)].text, redisstring, ex=59)
    print("naar redis")
