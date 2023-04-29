from flask import Flask, redirect, url_for, request,render_template
import os
from model import generate_files,predict
import json

app = Flask(__name__)

def getResult(name,colonies):
   generate_files(name,colonies)
   result,confidence = predict()
   bacterias = ['B.subtilis', 'C.albicans', 'E.coli', 'P.aeruginosa','S.aureus']
   for key,value in result.items():
      # print(key,value)
      result[key] = (bacterias[value[0]],value[1])
   return result,confidence

@app.route('/')
def index():
   '''
   Endpoint fot home page.
   Deleting all colony images for fresh predictions.
   '''
   for i in os.listdir(os.path.join(os.getcwd(),'static','test','colonies')):
      os.remove(os.path.join(os.getcwd(),'static','test','colonies',i))
   return render_template('index.html')


@app.route('/result',methods = ['POST'])
def result():
   '''
   Endpoint for processing the post request containing images and colony coordinates
   '''
   if request.method == 'POST':
      f = request.files['image']
      # Converting coordinate values to list
      # x = list(map(float,request.form.to_dict()['x-coord'].split(',')))
      # y = list(map(float,request.form.to_dict()['y-coord'].split(',')))
      colonies = json.loads(request.form.to_dict()['colony'])
      print(colonies)

      # Saving image file and generating result
      f.save(os.path.join(os.getcwd(),'data',f.filename))
      result,confidence = getResult(f.filename,colonies)

      return render_template('result.html',result = result,confidence=confidence,images = os.listdir(os.path.join(os.getcwd(),'static','test','colonies')))
   
   else:
      print("Invalid request returning to main page")
      return redirect('/')

if __name__ == '__main__':
   app.run(debug = True)