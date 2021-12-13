import urllib.request as ur
import random
import os
import easygui as e
import time



def url_open(url):
    html = ''
    try:
        time.sleep(0.1)
        
        iplist = ['115.208.76.154:8118','39.137.69.7:8080','221.180.170.104:8080']

        proxy_support = ur.ProxyHandler({'http':random.choice(iplist)})
        opener = ur.build_opener(proxy_support)
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36')]

        ur.install_opener(opener)
        
        response = ur.urlopen(url)
        html = response.read()
    except:
        print('访问错误')

    return html

def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']',a)

    return html[a:b]


def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('data-original')

    while a != -1:
        b = html.find('.jpg',a,a+255)
        if b != -1:
            img_addrs.append(html[a+15:b+4])
        else:
            b = a + 15

        a = html.find('data-original',b)
    '''for each in img_addrs:
        print(each)
    '''
    return img_addrs

def find_name(url):
    html = url_open(url).decode('utf-8')

    a = html.find('text-center') + 23
    b = html.find('</p>',a)

    return html[a:b]

def save_imgs(name,folder,img_addrs):
    if not os.path.exists('.' + '\\' + name):
        os.mkdir(name)
    os.chdir(name)
    
        
    for each in img_addrs:
        filename = each.split('/')[-1]
        print('成功下载了一张')
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)
            
    os.chdir('..')

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
    reply = e.buttonbox('这是一个自动抓取sexy照片的程序\n\n提示：图片会保存在该应用程序目录下\n\n你想开始吗？\n\n\n\n!!!!!!!!!!程序可能运行20秒左右，稍微耐心一点呦，mua~', \
                         choices = choices)
    if reply == choices[1] or reply == None:
        pass
    else:
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)

        pages = e.enterbox('请输入您总共想爬多少页:\n\n警告：最好是一个小于100的数字' )
        pages = int(pages)
        
        for i in range(pages):
            print('正在下载第%d页，进度：%d/%d' %(i+1,i+1,pages))
            page_url = 'https://qiukk54.com/arthtml/' + str(18167-i) + '.html'
            imgs_name = find_name(page_url)
            img_adds = find_imgs(page_url)
            save_imgs(imgs_name,folder,img_adds)
        now_dir = os.getcwd()
        os.chdir('..')
        e.msgbox('抓取完毕\n\n存放目录为：%s\n\n' % now_dir)


if __name__ == '__main__':
    dowmload_mm()
        
        
