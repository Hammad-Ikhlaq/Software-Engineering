import cv2
from face_detection import face
from keras.models import load_model
import numpy as np
from tkinter import *
from tkinter import Button 
from tkinter import Label
from tkinter import messagebox 
#from tkMessageBox import *
from embedding import emb
import pandas as pd
import re
from datetime import datetime
from fb import markAttend
import time

"""
Name of Programmer: Satinder (Open Source Code)
Job: This Script runs constantly to detect and predict employees and marks their entry attendence
Possible Failure : As Image quality is important images with low resolution may not get 
predicted accurately and wrong prediction is a high possibility in that case
"""
label=None

f = open("attendanceDict.txt", "r");
linesList = [];
if f.mode == 'r':
        linesList = f.readlines();
f.close();

attendanceDict={}

for line in linesList:
    tokens = re.split("\t", line);
    attendanceDict[int(tokens[0])]= int(tokens[1])



people={1:"sabir",2:"tahir",3:"hassan"}
e=emb()
fd=face()

model=load_model('face_reco2.MODEL')


def test():
    test_run=cv2.imread('1.jpg',1)
    test_run=cv2.resize(test_run,(160,160))
    test_run=test_run.astype('float')/255.0
    test_run=np.expand_dims(test_run,axis=0)
    test_run=e.calculate(test_run)
    test_run=np.expand_dims(test_run,axis=0)
    test_run=model.predict(test_run)[0]

def saveToFile():
    f = open("attendanceDict.txt", "w");
    for x in attendanceDict:
        f.write(str(x) + "\t" + str(attendanceDict[x])+ "\n")
    f.close();
	
	
	
cap=cv2.VideoCapture(0)
ret=True
#test()
while ret:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    det,coor=fd.detectFace(frame)

    if(det is not None):
        for i in range(len(det)):
            detected=det[i]
            k=coor[i]
            f=detected
            detected=cv2.resize(detected,(160,160))
           
            detected=detected.astype('float')/255.0
            detected=np.expand_dims(detected,axis=0)
            feed=e.calculate(detected)
            feed=np.expand_dims(feed,axis=0)
            prediction=model.predict(feed)[0]

            result=int(np.argmax(prediction))
            
            if(np.max(prediction)>.70):
                for j in people:
                    if(result==j):
                        label=people[j]
                        if(attendanceDict[j]==0):
                            print("Attendance marked of:" + label)
                            now = datetime.now()
                            hour=now.hour
                            minute=now.minute
                            day=now.day
                            month=now.month
                            year=now.year
                            markAttend(j,day,month,year,minute,hour,day,month,year,minute,hour)
                            attendanceDict[j]=1
                            saveToFile()
                            
                            message_window = Tk()
                            message_window.geometry("200x200")
                            
                            messagebox.showinfo("Notification","Attendance has been Marked  "+label)                            
                             
                            message_window.withdraw()
                            
                            
						
						
            else:
                label='unknown'
            
            
            cv2.putText(frame,label,(k[0],k[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
            
            cv2.rectangle(frame,(k[0],k[1]),(k[0]+k[2],k[1]+k[3]),(252,160,39),3)
            
    cv2.imshow('frame',frame)
    if(cv2.waitKey(1) & 0XFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

