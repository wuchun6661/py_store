import urllib.request as ur
import chardet

def main():
    url = input('请输入URL：')
    
    response = ur.urlopen(url)
    html = response.read()

    encode = chardet.detect(html)['encoding']
    if encode == "GB2312":
        encode = "GBK"

    print(encode)

if __name__ == '__main__':
    main()
