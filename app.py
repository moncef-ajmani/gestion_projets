from flask import Flask, redirect, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('dashboard.html')

# Add Routes
from projects import projects
from employees import employees

app.register_blueprint(projects,url_prefix='/projects')
app.register_blueprint(employees,url_prefix='/employees')


if __name__ == '__main__':
    app.run(debug=True)

