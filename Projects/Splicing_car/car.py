import numpy as np
import imutils
import cv2
import sys


def play():
    
    img1 = connect()
    
    img1 = my_resize(img1,1,1)
    img1_black = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,(0,0,0))#加黑边
    
    gray = cv2.cvtColor(img1_black,cv2.COLOR_RGB2GRAY)#灰度值
    thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)[1]#二值化，大于0的都变成255

    hang = thresh.shape[1]
    lie = thresh.shape[0]
    

    
    
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)#找外轮廓
    cnts = imutils.grab_contours(cnts)#返回cnts中的countors

    c = max(cnts, key=cv2.contourArea)#抓取最大区域的轮廓(原图像路轮廓)
    mask = np.zeros(thresh.shape, dtype="uint8")#为mask分配内存

    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(mask,(x,y),(x+w,y+h),255,-1)

    minRect = mask.copy()
    sub = mask.copy()
    
    while cv2.countNonZero(sub) > 10:#有非0数(白像素)则循环
        minRect = cv2.erode(minRect, None)
        sub = cv2.subtract(minRect, thresh)

    cnts = cv2.findContours(minRect.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    c = max(cnts, key=cv2.contourArea)
    (x, y, w, h) = cv2.boundingRect(c)

    img1_black = img1_black[y:y+h,x:x+w]



    
    cv2.imshow("Splicing_Result",img1_black)
    cv2.imwrite("./Splicing_Result.jpg",img1_black)

def my_resize(img,x,y):
    resized = cv2.resize(img,(    int(img.shape[1]*x),int(img.shape[0]*y)   )   )
    return resized


def connect():

    imgs = []
    
    img1 = cv2.imread("./car.jpg") 
    
    for i in range(1,8):#[1,8)
        file_name = "./photos/%s.jpg"%(i)
        img1 = cv2.imread(file_name)
        
        imgs.append(img1)
    
    
    stitcher = cv2.Stitcher.create(cv2.Stitcher_PANORAMA)

    (status,pano) = stitcher.stitch(  imgs  )
    if status != cv2.Stitcher_OK:
        print("不能拼接图片, error code = %d" % status)
        sys.exit(-1)

    print("拼接成功!")


    pano = my_resize(pano,0.25,0.25)
    cv2.imshow("pano",pano)
    
    
    return pano

    cv2.waiKey(0)
    
def test():    
    img1 = cv2.imread("./car.jpg")

    img2 = img1[0:1200,0:int(1920*0.5)]
    img3 = img1[0:1200,int(1920*0.25):int(1920*0.75)]
    img4 = img1[0:1200,int(1920*0.5):int(1920)]


    cv2.imshow("2",img2)
    cv2.imshow("3",img3)
    cv2.imshow("4",img4)

#test()

play()
