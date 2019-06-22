from flask import Flask, render_template, request
app = Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['GET','POST'])
def result():
   result = request.form
   return render_template('result.html',result = result)

if __name__ == '__main__':
   app.run(debug = True)

