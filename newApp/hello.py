from flask import Flask, redirect, url_for, request,render_template
import os
from model import generate_files,predict

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   generate_files(name)
   bacteria = predict()
   bacterias = ['B.subtilis', 'C.albicans', 'E.coli', 'P.aeruginosa','S.aureus']
   return '<html><body><h1>Image contains {}.</h1></body></html>'.format(bacterias[bacteria[0]])

@app.route('/')
def index():
   for i in os.listdir(os.path.join(os.getcwd(),'test','colonies')):
      print(i)
      os.remove(os.path.join(os.getcwd(),'test','colonies',i))
   return render_template('login.html')


@app.route('/login',methods = ['POST', 'GET'])
def login():

   if request.method == 'POST':
      print(type(request))
      f = request.files['image']
      f.save(os.path.join(os.getcwd(),'data',f.filename))
      # return redirect('/')
      return redirect(url_for('success',name = f.filename))
   else:
      print("returning to main page")
      return redirect('/')

if __name__ == '__main__':
   app.run(debug = True)