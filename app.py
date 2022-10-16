from select import select
from flask import Flask, render_template
import mysql.connector

connection = mysql.connector.connect(
    host='localhost', port=3306, database='StudentsRecords', user='root', password='', auth_plugin='mysql_native_password')

cursor = connection.cursor()

app = Flask(__name__)


@app.route('/')
def index():
    return "hello world"


@app.route("/display")
def display():
    cursor.execute("select * from StudentsRecords.Students")
    value = cursor.fetchall()
    return render_template('index.html', data=value, name="Students Data")


if __name__ == '__main__':
    app.run(debug=True)
