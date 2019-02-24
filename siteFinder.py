import requests
from lxml import html
import time
import random
import time
# from request_helper import *
base = 'https://www.google.com/search?q='
keywords = open('sites.txt', 'r').read()
IGNORE = ['facebook', 'wikipedia', 'youtube', 'twitter', 'linkedin', 'indeed']

keywords = [_.strip() for _ in keywords.split('\n') if _.strip()]
with open("final_data.txt", "w") as fp:
    for key in keywords[0:100]:
        url = base + key
        # resp = get_response(url, use_proxy=False)
        resp = requests.get(url)
        delay = random.randint(2, 7)
        print(delay)
        time.sleep(delay)
        # open('abc.html', 'wb').write(resp.content)
        page = html.fromstring(resp.content)
        links = page.xpath('//div[@id="search"]//ol//h3/a/@href')
        final_link = ''
        for link in links:
            if not any([c for c in IGNORE if c in link]):
                link = link.replace('/url?q=', '')
                link = link.replace('https://', '')
                link = link.replace('www.', '')
                link = link.split('/')[0]
                print(link)
                final_link = link
                break
        line = key + "$$" + final_link + "\n"
        fp.write(line)
        
    