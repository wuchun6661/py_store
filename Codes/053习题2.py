import chardet
import urllib.request as ur

def main():
    i = 0

    with open("urls.txt",'r') as f:
        urls = f.read().splitlines()

    for each_url in urls:
        response = ur.urlopen(each_url)
        html = response.read()

        encode = chardet.detect(html)['encoding']
        if encode == 'GB2312':
            encode = 'GBK'

        i += 1
        file_name = 'url_%d.txt' % i

        with open(file_name,'w',encoding=encode) as each_file:
            each_file.write(html.decode(encode,"ignore"))

if __name__ == '__main__':
    main()
        
