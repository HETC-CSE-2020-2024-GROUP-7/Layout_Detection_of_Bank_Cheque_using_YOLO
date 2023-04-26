import numpy as np
import cv2 as cv 
import csv
import os
global img_path
global blank
global arr
global p
global nameOfClasses
global points
global backSpaceFlag
HEIGHT = 540; WIDTH = 960
blank = -1-1j
arr = np.full(shape=(4,4),fill_value=blank)
p = np.full(shape=(4,), fill_value=1,dtype=int)
nameOfClasses = np.array(["Signature","Date","Amount","AcNo"])
points = "ABCD"
backSpaceFlag = False

global curImg 
global prevImg
global round; 
global count; 

def make_blank(i):
     arr[i] = np.full(shape=(4,), fill_value=blank)
def complex2xy(c:complex):
    return c.real,c.imag
def write(img):        
    with open("./data.csv",'a') as f:
        writer = csv.writer(f)       
        for i in range(4):
            ax,ay=complex2xy(arr[i][0])
            bx,by=complex2xy(arr[i][1])
            cx,cy=complex2xy(arr[i][2])
            dx,dy=complex2xy(arr[i][3])
            l = [img_path,*img.shape[:2],nameOfClasses[i],p[i],ax,ay,bx,by,cx,cy,dx,dy]
            writer.writerow(l)
def clickEvent(ev,x,y,f,params):  
    global round; 
    global count;   
    global arr; 
    global curImg 
    global prevImg
    global backSpaceFlag
    if ev==cv.EVENT_LBUTTONDOWN:
        if(round<4 and count<4):            
            backSpaceFlag=True
            print(f"Class : {nameOfClasses[round]}, Cordinate:{points[count+1]}")
            a = complex(x,y);count+=1; 
            arr[round,count]=a
            prevImg = np.array(curImg)
            cv.circle(curImg,(int(a.real),int(a.imag)),2,(0,0,255),2)
            cv.resizeWindow("img", WIDTH, HEIGHT)
            cv.imshow("img",curImg)            
            print(round,count)
            if(count==3):
                round+=1;count = -1 
        else:
            print("4*4 = 16 cordinate is collected please write by pressing Enter or clear using BackSpace\n To print the data press space ")
def extract(img_path,HEIGHT=540,WIDTH=960):
    global round; 
    global count;   
    global arr; 
    global curImg 
    global prevImg
    global backSpaceFlag
    global blank
    global arr
    global nameOfClasses
    cv.namedWindow("img", cv.WINDOW_NORMAL)
    round,count=0,-1 
    img = cv.imread(img_path)
    prevImg,curImg = np.array(img),np.array(img)
    cv.resizeWindow("img", WIDTH, HEIGHT)
    cv.imshow("img",img)
    cv.setMouseCallback('img',clickEvent)
    while True:
        k=cv.waitKey(0)
        print(k)
        if k==255:
            arr=np.full(shape=(4,4),fill_value=blank)
            round=0; 
            count=-1; 
            curImg=np.array(img)
            cv.resizeWindow("img", WIDTH, HEIGHT)
            cv.imshow("img", curImg) 
            print("All point ar discard start from begin")
        if k == 9:
            if round < 4:
                print(f"class {nameOfClasses[round]} is skiped")
                p[round]=0;round+=1;count= -1; 
            else :
                print("Round is completed Press delete for restart round or press enter to save")   
        if k == 8 and backSpaceFlag:
            backSpaceFlag = False
            if round ==4 :
                round=3;count=2; 
                arr[3,3]=blank
            else:
                arr[round,count]=blank
                if count == -1 and round == 0:
                    print("No Previous Condition found")
                elif count == -1 and round > 0:
                    round-=1; count=2            
                else:
                    count-=1        
            print(round, count)
            curImg = np.array(prevImg)   
            cv.resizeWindow("img", WIDTH, HEIGHT)
            cv.imshow('img',curImg)
        if k == 32: 
            print(arr)
        if k==13:
            y='y'
            if round<4:
                y=input("All data points are not collected\nDo you want to write?(y/n):")
            if y=='y' or y == 'Y':
                write(img)
            break
        if k==27 or k==113 :        
            break
    cv.destroyAllWindows()


def extract_data_in_loop(data_dir, csv_path = "data.csv", start=0,end = -1):
    path_list = [os.path.join(data_dir, i) for i in os.listdir(data_dir)]
    for img_path in path_list[start:end]:
        extract(img_path)
        print(f"{img_path} data is stored.")
        n = input("Continue ? : ")
        if n == "N" or n=='n':
            break



# Set the image folder location here
extract_data_in_loop(r'/home/aritrarc/Pictures/Screenshots')
