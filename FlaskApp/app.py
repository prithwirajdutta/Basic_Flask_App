from flask import Flask, render_template, request
from flask_mail import Mail, Message
from flask_mysqldb import MySQL

app = Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['GET','POST'])
def result():
   result = request.form
   return render_template('result.html',result = result)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'

mysql = MySQL(app)

@app.route('/insertdata')
def insertdata():
        id = "505"
        name = "Prithwiraj"
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO testingtb(id, name) VALUES (%s, %s)", (id, name))
        mysql.connection.commit()
        cur.close()
        return 'success'

@app.route('/displaydata')
def displaydata():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM testingtb''')
    rv = cur.fetchall()
    return str(rv)



if __name__ == '__main__':
   app.run()

