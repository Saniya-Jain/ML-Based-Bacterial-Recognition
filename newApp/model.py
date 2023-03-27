from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
import numpy as np
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from collections import Counter
from numba import jit
import cv2
import os
import shutil
modelFile = 'D:/Users/Krutik/College/LY/FinalProject/code/Approach2/MobileNet-weights-best.h5'
fPath = os.path.join(os.getcwd(),'test')
# this is the augmentation configuration we will use for validating
val_datagen = ImageDataGenerator(rescale=1./255)
model = load_model(modelFile)

@jit
def predict():
    
    #this generates batches of augment data for validating
    validation_flow = val_datagen.flow_from_directory(
        fPath,
        target_size=(256, 256),
        batch_size=32,
        class_mode= 'categorical',
        shuffle = False)

    y_pred = model.predict(validation_flow)
    pred_labels = np.argmax(y_pred, axis = 1)
    data = Counter(pred_labels)
    print(data)
    return data.most_common(1)[0]

def crop_colony(image,x,y):
  # Setting the points for cropped image
  left = x
  top = y 
  right = x + 256
  bottom = y + 256
  print(left,right,top,bottom)
  # Cropped image of above dimension
  # (It will not change original image)
  im1 = image[left:right,top:bottom]

  return im1

def generate_files(name):
   image = os.path.join(os.getcwd(),'data',name)
   res_path = os.path.join(os.getcwd(),'test','colonies',name)
   shutil.copyfile(image, res_path)
# #    print(image.shape)
#    height,width,_ = image.shape
#    h = height // 256
#    w = width // 256 
#    print(height,width,h,w)
#    counter = 1
#    for i in range(h):
#       for j in range(w):
#         filename = os.path.join(res_path,"{}.png".format(counter))
#         # image = crop_colony(image,256*j,256*i)
#         # if image.shape[0] == 256:
#         cv2.imwrite(filename,crop_colony(image,256*j,256*i))
#         counter += 1
