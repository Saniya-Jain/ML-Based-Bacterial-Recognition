from flask import Flask, redirect, url_for, request,render_template
import os
from model import generate_files,predict

app = Flask(__name__)

@app.route('/success/<data>')
def success(data,x,y):
   generate_files(data)
   bacteria = predict()
   bacterias = ['B.subtilis', 'C.albicans', 'E.coli', 'P.aeruginosa','S.aureus']
   # return '<html><body><h1>Image contains {}.</h1></body></html>'.format("None")
   return '<html><body><h1>Image contains {}.</h1></body></html>'.format(bacterias[bacteria[0]])
   # return  render_template('index.html')

@app.route('/')
def index():
   for i in os.listdir(os.path.join(os.getcwd(),'test','colonies')):
      print(i)
      os.remove(os.path.join(os.getcwd(),'test','colonies',i))
   return render_template('index.html')


@app.route('/login',methods = ['POST', 'GET'])
def login():

   if request.method == 'POST':
      # print(type(request))
      f = request.files['image']
      print(request.form.to_dict())
      x = float(request.form.to_dict()['x-coord'])
      y = float(request.form.to_dict()['y-coord'])
      print("data = ",request.form.to_dict())
      f.save(os.path.join(os.getcwd(),'data',f.filename))
      # return redirect('/')
      generate_files(f.filename,x,y)
      bacteria = predict()
      bacterias = ['B.subtilis', 'C.albicans', 'E.coli', 'P.aeruginosa','S.aureus']
      # return '<html><body><h1>Image contains {}.</h1></body></html>'.format("None")
      return '<html><body><h1>Image contains {}.</h1></body></html>'.format(bacterias[bacteria[0]])
      # return redirect(url_for('success',name = f.filename, x= x,y =y))
   else:
      print("returning to main page")
      return redirect('/')

if __name__ == '__main__':
   app.run(debug = True)