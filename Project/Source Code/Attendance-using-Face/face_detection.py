import cv2

'''
Name of Programmer: Satinder (Open Source Code)
Job: Has functions related to detection of a face within the image 
Possible Failure : As Image quality is important images with low resolution may not get 
		 detected accurately and wrong detection or no detection is a high possibility in that case
'''
class face:
    def __init__(self):
        self.cascade=cv2.CascadeClassifier('faces.xml')
        self.x=None
        self.y=None
        self.w=None
        self.h=None

    #takes an image as input and returns the cropped face image detected in that image 
    #with its coordinates in that image
    def detectFace(self,img):
        cropped=None
        grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=self.cascade.detectMultiScale(grey,1.3,5)
        cropped=[]
        coor=[]
        for (self.x,self.y,self.w,self.h) in faces:
            cropped.append(img[self.y:self.y+self.h,self.x:self.x+self.w])
            coor.append([self.x,self.y,self.w,self.h])
        return cropped,coor
