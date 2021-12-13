import urllib.request as ur
import urllib.parse as up
import json
def translate():
    while 1:
        str1 = input('请输入你要翻译的句子("w"退出)：')
        if str1 == 'w':
            print('已经退出翻译模式→_→')
            break
        else:
            url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
            head = {}
            head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'

            data = {}
            data['i'] = str1
            data['from'] = 'AUTO'
            data['to'] = 'AUTO'
            data['smartresult'] = 'dict'
            data['client'] = 'fanyideskweb'
            data['salt'] = '15832459480291'
            data['sign'] = '01ab6935101bc91550116d13082f00d6'
            data['ts'] = '1583245948029'
            data['bv'] = '35242348db4225f3512aa00c2f3e7826'
            data['doctype'] = 'json'
            data['version'] = '2.1'
            data['keyfrom'] = 'fanyi.web'
            data['action'] = 'FY_BY_CLICKBUTTION'

            data = up.urlencode(data).encode('utf-8')

            req = ur.Request(url,data,head)
            response = ur.urlopen(req)
            html = response.read().decode('utf-8')
            html = json.loads(html)

            print('翻译结果：%s' % html['translateResult'][0][0]['tgt'])

if __name__ == "__main__":
    translate()
