import urllib.request as ur
import random

url = 'http://45.32.164.128/ip.php'

iplist = ['115.208.76.154:8118','39.137.69.7:8080','221.180.170.104:8080']

proxy_support = ur.ProxyHandler({'http':random.choice(iplist)})

opener = ur.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36')]

ur.install_opener(opener)

response = ur.urlopen(url)
html = response.read().decode('gbk')

print(html)
