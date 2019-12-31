from keras.models import load_model

'''
Name of Programmer: Satinder (Open Source Code)
Job: Has functions related loading facenet model and predicting face using that model 
Possible Failure : As Image quality is important images with low resolution may not get 
		 predicted accurately and wrong prediction is a high possibility in that case
'''
class emb:
    def __init__(self):
        self.model=load_model('facenet_keras.h5')
		
	#predicts the class of image which was taken as input	
    def calculate(self,img):
        return self.model.predict(img)[0]
