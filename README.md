# BitcoinTransactionScraper

!MAKE SURE PYTHON3 IS INSTALLED!
If not, use `sudo apt-get install python3` to do so.

Requirements:
- pip3: `sudo apt-get install python3-pip`
- requests: `pip3 install requests`
- beautifulsoup4: `pip3 install bs4`
- pymongo: `pip3 install pymongo`
- redis: `pip3 install redis`

First install mongoDB by running `bash installermongo`.

Then install redis by running `bash installerredis`.

To run excecute `python3 bitcoin.py`. All logs will be added to the mongoDB.

Proof that it works:
- Lesson 2 (MongoDB): `works.PNG`
- Lesson 3 (redis): `worksredis.png`
