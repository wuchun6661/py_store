import cv2
import argparse
import os
import time as t
def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='Process pic')
    parser.add_argument('--input', help='video to process', dest='input', default=None, type=str)
    parser.add_argument('--output', help='pic to store', dest='output', default=None, type=str)
    #default为间隔多少帧截取一张图片
    parser.add_argument('--skip_frame', dest='skip_frame', help='skip number of video', default=100, type=int)
    #input为输入视频的路径 ，output为输出存放图片的路径
    args = parser.parse_args(['--input','./test.mp4','--output','./photos','--skip_fram','1'])
    return args

def process_video(i_video, o_video, num):
    cap = cv2.VideoCapture(i_video)
    num_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    expand_name = '.jpg'
    if not cap.isOpened():
        print("Please check the path.")
    cnt = 0
    count = 0
    while 1:
        ret, frame = cap.read()
        cnt += 1
        #  how
        # many
        # frame
        # to
        # cut
        if cnt % num == 0:
            count += 1
            print(cnt,count)
            cv2.imwrite(os.path.join(o_video, str(count) + expand_name), frame)

        if not ret:
            break
        
def play():
    pictures = []
    cap = cv2.VideoCapture(1)
    while 1:
        ret,frame = cap.read()
        if frame is not None:
            #frame = cv2.resize(frame, ( int(frame.shape[1]/2),int(frame.shape[0]/2))  )
            cv2.imshow("Video",frame)
            k = cv2.waitKey(1) & 0xff
            if k == ord('q'):
                break
            if k == ord('s'):
                file_name = "./" +  t.strftime("%d %b %Y %H %M %S",t.localtime())    + '.jpg'
                print(file_name)
                cv2.imwrite( file_name ,frame )

            file_name = "./" +  t.strftime("%d %b %Y %H %M %S",t.localtime())    + '.jpg'
            pictures.append([file_name,frame])        
    cap.release()
    cv2.destroyAllWindows()

    for [file_name,frame] in pictures:
        cv2.imwrite( file_name ,frame )

play()

'''
if __name__ == '__main__':
    args = parse_args()
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    print('Called with args:')
    print(args)
    process_video(args.input, args.output, args.skip_frame)
'''
