import numpy as np
import imutils
import cv2
import sys
import matplotlib.pyplot as plt
import time

def catch_point():

    img1 = cv2.imread("./photos/98.jpg")
    img2 = cv2.imread("./photos/99.jpg")

    img1 = my_resize(img1,  0.35,   0.35)
    img2 = my_resize(img2,  0.35,   0.35)
    
    surf = cv2.xfeatures2d.SURF_create(20) #实例化
    
    kp1,des1 = surf.detectAndCompute(img1,None)#找出关键点
    kp2,des2 = surf.detectAndCompute(img2,None)
    
    #img3 = cv2.drawKeypoints(img1,kp1,None,None)#圈出关键点

    bf = cv2.BFMatcher()
    
    matches = bf.knnMatch(des1, des2, k=2)

    img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

    plt.imshow(img3),plt.show()
    
    #cv2.imshow("sift",img2)
    
    
def my_abs(x):
    if(x<0):
        x=-x
    return x


def my_resize(img,x,y):
    resized = cv2.resize(img,(  int(img.shape[1]*x),int(img.shape[0]*y) ))
    return resized
def test_2():
    img1 = cv2.imread('3.jpg')
    img2 = cv2.imread('2.jpg')

    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    # 初始化SURT检测器
    surf = cv2.xfeatures2d.SURF_create(20)
     
    # 用SIFT找到关键点和描述符
    kp1, des1 = surf.detectAndCompute(img1, None)
    kp2, des2 = surf.detectAndCompute(img2, None)
     
    # 默认参数的BFMatcher
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2,k=2)  #(queryIdx,trainIdx,distance)
     
    # 应用比率测试(ratio test)
    good = []
    good2 = []
    for m, n in matches:
        if m.distance < 0.6 * n.distance:
            good.append([m])
            good2.append(m)
          
    if len(good) > 4:
        pts1 = np.float32([ kp1[m.queryIdx].pt for m in good2 ])
        pts2 = np.float32([ kp2[m.trainIdx].pt for m in good2 ])
    

        (H, status) = cv2.findHomography(pts1,pts2,cv2.RANSAC,4.0)#(第四个参数1-10，原图像的点经过变换后点与目标图像上对应点的误差)

    result = cv2.warpPerspective(img1,H, (img1.shape[1] + img2.shape[1], img1.shape[0])  )

    result[     0:img2.shape[0], 0: img2.shape[1]   ] = img2

    img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
                                              
    plt.imshow(result), plt.show()

def mix_and_match(leftImage, warpedImage):
    i1y, i1x = leftImage.shape[:2]
    i2y, i2x = warpedImage.shape[:2]

    black_l = np.where(leftImage == np.array([0,0,0]))
    black_wi = np.where(warpedImage == np.array([0,0,0]))

    for i in range(0, i1x):
        for j in range(0, i1y):
            try:
                if(np.array_equal(leftImage[j,i],np.array([0,0,0])) and  np.array_equal(warpedImage[j,i],np.array([0,0,0]))):
                    warpedImage[j,i] = [0, 0, 0]
                else:
                    if(np.array_equal(warpedImage[j,i],[0,0,0])):
                        warpedImage[j,i] = leftImage[j,i]
                    else:
                        if not np.array_equal(leftImage[j,i], [0,0,0]):
                            bw, gw, rw = warpedImage[j,i]
                            bl,gl,rl = leftImage[j,i]
                            warpedImage[j, i] = [bl,gl,rl]
            except:
                pass
            
    return warpedImage



    
def test():
    img1 = cv2.imread('./photos/104.jpg')
    img2 = cv2.imread('./car_1.jpg')

    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    # 初始化SURT检测器
    surf = cv2.xfeatures2d.SURF_create(20)
     
    # 用SIFT找到关键点和描述符
    kp1, des1 = surf.detectAndCompute(img1, None)
    kp2, des2 = surf.detectAndCompute(img2, None)
     
    # 默认参数的BFMatcher
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2,k=2)  #(queryIdx,trainIdx,distance)
     
    # 应用比率测试(ratio test)
    good = []
    good2 = []
    for m, n in matches:
        error_x = kp1[m.queryIdx].pt[0] - kp2[m.trainIdx].pt[0]
        error_y = kp1[m.queryIdx].pt[1] - kp2[m.trainIdx].pt[1]
        error_x = my_abs(error_x)
        error_y = my_abs(error_y)
        if error_x > 20 and error_y <50 and kp1[m.queryIdx].pt[0] > 100 and kp1[m.queryIdx].pt[1] > 1200 and kp1[m.queryIdx].pt[1] <  2400:
            if m.distance < 0.7 * n.distance:
                good.append([m])
                good2.append(m)
         
    if len(good) > 4:
        pts1 = np.float32([ kp1[m.queryIdx].pt for m in good2 ])
        pts2 = np.float32([ kp2[m.trainIdx].pt for m in good2 ])
    

        (H, status) = cv2.findHomography(pts1,pts2,cv2.RANSAC,4.0)#(第四个参数1-10，原图像的点经过变换后点与目标图像上对应点的误差)

   
    
    result = cv2.warpPerspective(img1,H, (img1.shape[1] + img2.shape[1], img1.shape[0])  )
    result = mix_and_match(img2,result)
    #result[     0:img2.shape[0], 0: img2.shape[1]   ] = img2
    
    img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
                                                    #,singlePointColor=(0,255,0),matchColor= 'Default')
    
    plt.imshow(result), plt.show()
    '''
    result = cv2.cvtColor(result,cv2.COLOR_BGR2RGB)
    cv2.imwrite("./car_2.jpg",result)
    '''
    
test()

