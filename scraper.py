from bs4 import BeautifulSoup
import requests
import time

def scrape():
    url = 'https://www.blockchain.com/btc/unconfirmed-transactions'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    #print(soup.prettify())

    has = soup.find_all('a',{ "class" : "sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK"})
    allebs = soup.find_all('span',{ "class" : "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"})

    #for x in range(len(allebs)):
    #    if(x%3 == 0):
    #        print(allebs[x].text)
    #    if(x%3 == 1):
    #        print(allebs[x].text[:-4])
    #    if(x%3 == 2):
    #        print(allebs[x].text[1:])

    tel = 0
    for x in range(0, len(allebs)):
        if(x%3 == 1):
            if (float(allebs[x].text[:-4]) > float(allebs[tel].text[:-4])):
                tel = x
    
    string = has[(tel-1)%3].text + ' | ' + allebs[tel-1].text + ' | ' + allebs[tel].text + ' | ' + allebs[tel+1].text
    f = open("LogBitcoin.txt", "a")
    f.write("\n")
    f.write(string)
    f.close()

try:
    f = open("LogBitCoin.txt", "x")
    f.close()
    f = open("LogBitcoin.txt", "a")
    f.write("BitcoinTransactionScraper Logfile")
    f.write("\n")
    f.write("HASH | TIME | AM_BTC | AM_USD")
    f.write("\n")
    f.write("==============================================")
    f.close()
except:
    print("File already exists. Adding new logs.")

while True:
    scrape()
    time.sleep(60)
