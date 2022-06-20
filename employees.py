from flask import Blueprint, render_template

employees = Blueprint('employees', __name__)

@employees.route('/')
def index():
    return render_template('employee/index.html')

@employees.route('/create')
def create():
    return render_template('employee/create.html')

@employees.route('/show/<int:id>')
def show(id):
    return render_template('employee/show.html')

@employees.route('/edit/<int:id>')
def edit(id):
    return render_template('employee/edit.html')