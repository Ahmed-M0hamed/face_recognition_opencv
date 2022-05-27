import os 
import cv2
from numpy import imag 

images_path = os.path.join(os.getcwd(),'scrabed_data', 'images')

for file in os.listdir(images_path) : 
    if os.path.exists(os.path.join(images_path , file)) : 
        image = cv2.imread(os.path.join(images_path , file)) 
        # print(image.shape)
        if (image.shape[0] > 300) & ( image.shape[1] > 450) : 
            resized = cv2.resize(image , (450 , 300)) 
            cv2.imwrite(os.path.join('F:/opencv_face_detection' , 'resized_data','images' , file) , resized) 
        else : 
            print('image dims are not suitable') 
    else : 
        print('file is not exist')
