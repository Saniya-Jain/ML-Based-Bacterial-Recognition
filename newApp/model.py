from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
import numpy as np
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from collections import Counter
import cv2
import os
import shutil
from PIL import Image,ImageDraw

''' Loading Models for prediction '''
models = []
modelPath = 'D:/Users/Krutik/Projects/finalProject/src/models'
modelFiles = os.listdir(modelPath)
for modelFile in modelFiles[4:]:
    models.append((load_model(modelPath + '/' +modelFile),modelFile.split('.')[0].split("-")[0]))
fPath = os.path.join(os.getcwd(),'static','test')
# this is the augmentation configuration we will use for validating
val_datagen = ImageDataGenerator(rescale=1./255)

def predict():

    '''
    Function to make prediction on selected images and store their results in tabular format.
    '''

    result = {}

    #this generates batches of augment data for validating
    validation_flow = val_datagen.flow_from_directory(
        fPath,
        target_size=(256, 256),
        batch_size=32,
        class_mode= 'categorical',
        shuffle = False)
    
    total = 0
    for model in models:
        # n = number of images selecter by user
        # y_pred gives prediction for all images from one model - matrix of size n*5
        y_pred = model[0].predict(validation_flow)

        # pred_label contains maximum probability of prediction of each image - array of size n*1
        pred_label = np.argmax(y_pred, axis=1)
        
        # Storing result in dataframe as tabular format
        for i in range(len(os.listdir(fPath+'\\colonies'))):
            total += y_pred[i][pred_label[i]]
            result[i] = (pred_label[i],y_pred[i][pred_label[i]],model[1])
    
    return result,round(total/5,5)


def generate_files(name,colonies):

    '''
    Function to generate colony specific images that will pe used for prediction.
    '''

    image_path = os.path.join(os.getcwd(),'data',name)
    count = 0
    # for x,y in zip(xCoords,yCoords):
        
    #     res_path = os.path.join(os.getcwd(),'static','test','colonies',"cropped-{}.png".format(count))
    #     if not os.path.exists(os.path.join(os.getcwd(),'static','test','colonies')):
    #         pass
    #     image = Image.open(image_path)
    #     width,height = image.size
        
    #     # Getting the exact coordinates of image to crop from original image
    #     x = (x*width)//500
    #     hcap = (height*500)/width
    #     y = (y*height)/hcap

    #     crop = image.crop((x,y-256,x+256,y))
    #     crop.save(res_path)
    #     count += 1
    image = Image.open(image_path)
    img = cv2.imread(image_path)
    width,height = image.size

    for col, coords in colonies.items():
        
        res_path = os.path.join(os.getcwd(),'static','test','colonies',"cropped-{}.png".format(col))
        res_path_2 = os.path.join(os.getcwd(),'static','test','colonies',"cropped-cv-{}.png".format(col))
        if not os.path.exists(os.path.join(os.getcwd(),'static','test','colonies')):
            pass
        
        
        # Getting the exact coordinates of image to crop from original image
        x = (coords[0]*width)//500
        hcap = (height*500)/width
        y = (coords[1]*height)/hcap

        crop = image.crop((x,y-256,x+256,y))
        c_img = img[x:x+256,y:y-256]
        cv2.imwrite(res_path_2,c_img)
        # crop = crop.resize(256,256)
        crop.save(res_path)
        count += 1
