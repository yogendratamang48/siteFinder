import requests
from lxml import html
import time
import random
import time
import selenium
from selenium import webdriver
# from request_helper import *
base = 'https://www.google.com/search?q='
keywords = open('sites.txt', 'r').read()
IGNORE = ['facebook', 'wikipedia', 'youtube', 'twitter', 'linkedin', 'indeed']
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'}
keywords = [_.strip() for _ in keywords.split('\n') if _.strip()]
driver = webdriver.Firefox()
with open("final_data.txt", "a") as fp:
    for key in keywords[100:155]:
        url = base + key
        # resp = get_response(url, use_proxy=False)
        print(url)
        # resp = requests.get(url, headers=headers)
        driver.get(url)
        delay = random.randint(2, 7)
        print(delay)
        time.sleep(delay)
        # open('abc.html', 'wb').write(resp.content)
        #page = html.fromstring(resp.content)
        page = html.fromstring(driver.page_source.encode('utf-8'))
        links = page.xpath('//div[@id="search"]//cite/text()')
        final_link = ''
        for link in links:
            if not any([c for c in IGNORE if c in link]):
                link = link.replace('/url?q=', '')
                link = link.replace('https://', '')
                link = link.replace('www.', '')
                link = link.split('/')[0]
                # print(link)
                final_link = link
                break
        print(final_link)
        line = key + "$$" + final_link + "\n"
        fp.write(line)
driver.close()
