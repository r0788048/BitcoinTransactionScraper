import time
import scraper
import parser

while True:
    scraper.scrape()
    parser.loaddb()
    time.sleep(59)
