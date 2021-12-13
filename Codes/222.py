import urllib.request as ur
import random
import os
import easygui as e
import time


def url_open(url):
    print(url)
    time.sleep(1)
    req = ur.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36")
    #req.add_header("Referer","https://qiukk54.com/arthtml/18167.html")
    #req.add_header("Sec-Fetch-Dest","image")
    
    response = ur.urlopen(req)
    html = response.read()

    html2 = html.decode('utf-8')
    print(html2)
    return html
