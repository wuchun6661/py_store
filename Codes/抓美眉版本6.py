import urllib.request as ur
import random
import os
import easygui as e
import time



def url_open(url):
    time.sleep(1)
    req = ur.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36")

    iplist = ['115.208.76.154:8118','39.137.69.7:8080','221.180.170.104:8080']
    proxy = random.choice(iplist)

    '''
    proxy_support = ur.ProxyHandler({'http':proxy})
    opener = ur.build_opener(proxy_support)
    ur.install_opener(opener)
     '''
    response = ur.urlopen(url)
    html = response.read()

    return html

def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']',a)

    return html[a:b]


def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg',a,a+255)
        if b != -1:
            img_addrs.append('http:' + html[a+9:b+4])
        else:
            b = a + 9

        a = html.find('img src=',b)
    for each in img_addrs:
        print(each)
    return img_addrs


def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        print('成功下载了一张')
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)

def dir_urls(url,n):
    list1 = [url]
    while n:
        html = url_open(url).decode('utf-8')
        a = html.find('current-comment-page')
        b = html.find('a href=',a,a+255)
        c = html.find('">',b,b+255)
        list1.append('http:' + html[b+8:c])
        
        url = 'http:' + html[b+8:c]
        n -= 1
    return list1

def dowmload_mm(folder='OOXX'):
    choices = ('兴奋死了，快开始','不要，我拒绝！')
    reply = e.buttonbox('这是一个自动抓取漂亮美眉的程序\n\n提示：图片会保存在该应用程序目录下\n\n你想开始吗？\n\n\n\n!!!!!!!!!!程序可能运行20秒左右，稍微耐心一点呦，mua~',choices = choices)
    if reply == choices[1] or reply == None:
        pass
    else:
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)

        url = "http://jandan.net/ooxx"
        page_num = int(get_page(url))
        pages = e.enterbox('总共%d页，请输入您总共想爬多少页:\n\n警告：输入的整数值不能超过%d！！！' % (page_num,page_num))
        pages = int(pages)
        
        for i in range(pages):
            page_url = dir_urls('http://jandan.net/ooxx',pages)[i]
            img_adds = find_imgs(page_url)
            save_imgs(folder,img_adds)
        now_dir = os.getcwd()
        e.msgbox('抓取完毕\n\n存放目录为：%s\n\n→_→' % now_dir)


if __name__ == '__main__':
    dowmload_mm()
        
        
