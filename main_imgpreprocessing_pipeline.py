import cv2
from PIL import Image
from rembg import remove
import os


for i in (10):
    input = Image.open(str(i)+'.jpg')
    output = remove(input)
    output.save(str(i)+"temp.png")
    img = cv2.imread(str(i)+"temp.png")
    gray = cv2.ctColor(img,cv2.COLOR_BG2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 551, 8.6)
    contours, _ = cv2.findContours(thresh, cv2.RET_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x, y, h, w = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), -1)
    img = cv2.resize(img, (350,350))

    filename = "final/"+str(i)+".png"
    cv2.imwrite(filename, img)
    os.remove(str(i) + "temp.png")
    print(str(i) + ":done")
