import urllib.request as ur
import chardet
import easygui as e
import os

def catch_cat():
    while 1:
        fields = ['长','宽']
        choices1 = ('逼话少说，开始！','不开始！')
        choices2 = ('逼话少说，继续！','溜了溜了')

        e.msgbox('欢迎来到抓猫咪图片小程序','抓猫咪图片')
        size = e.multenterbox('长和宽输入都必须为整数！','尺寸选择',fields = fields)
        dir_cat = e.diropenbox()

        reply1 = e.buttonbox('开始抓取吗？',choices=choices1)
        if reply1 == '不开始':
            break
        else:
            response = ur.urlopen("http://placekitten.com/%s/%s" % (str(size[0]),str(size[1])) )
            cat_img = response.read()

            with open(dir_cat + os.sep + 'cat(%sX%s).jpg' % (str(size[0]),str(size[1])) ,'wb') as f:
                f.write(cat_img)
            e.msgbox('抓取成功！')

            reply2 = e.buttonbox('是否继续？',choices = choices2)
            if reply2 == '溜了溜了':
                break

if __name__ == '__main__':
    catch_cat()
