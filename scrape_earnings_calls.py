# scrape.py
# scrapes earning call data from Seeking Alpha

import requests
import time
from bs4 import BeautifulSoup

def get_date(c):
    end = c.find('|')
    return c[0:end-1]

def get_ticker(c):
    beg = c.find('(')
    end = c.find(')')
    return c[beg+1:end]

def grab_page(url):
    print("attempting to grab page: " + url)
    page = requests.get(url)
    page_html = page.text
    soup = BeautifulSoup(page_html, 'html.parser')

    meta = soup.find("div",{'class':'a-info get-alerts'})
    content = soup.find(id="a-body")

    if type(meta) or type(content) == "NoneType":
        print("skipping this link, no content here")
        return
    else:
        text = content.text
        mtext = meta.text

        filename = get_ticker(mtext) + "_" + get_date(mtext)
        file = open(filename.lower() + ".txt", 'w')
        file.write(text)
        file.close
        print(filename.lower()+ " sucessfully saved")

def process_list_page(i):
    origin_page = "https://seekingalpha.com/earnings/earnings-call-transcripts" + "/" + str(i)
    print("getting page " + origin_page)
    page = requests.get(origin_page)
    page_html = page.text
    #print(page_html)
    soup = BeautifulSoup(page_html, 'html.parser')
    alist = soup.find_all("li",{'class':'list-group-item article'})
    for i in range(0,len(alist)):
        url_ending = alist[i].find_all("a")[0].attrs['href']
        url = "https://seekingalpha.com" + url_ending
        grab_page(url)
        time.sleep(.5)

for i in range(1,200): #choose what pages of earnings to scrape
    process_list_page(i)
