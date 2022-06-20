from flask import Blueprint, render_template

projects = Blueprint('projects', __name__)

@projects.route('/')
def index():
    return render_template('projet/index.html')

@projects.route('/create')
def create():
    return render_template('projet/create.html')

@projects.route('/show/<int:id>')
def show(id):
    return render_template('projet/show.html')