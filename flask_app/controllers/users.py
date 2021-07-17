from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.users import User

@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', users=users)

@app.route('/users')
def users_table():
    return render_template('users.html')

@app.route('/users_select')
def users_select():
    return render_template('users_select.html')

@app.route('/users_edit')
def users_edit():
    return render_template('users_edit.html')

@app.route('/users/create/new', methods=['POST'])
def create_user():
    data = {
        'first_name': request.form['first_name'],'last_name': request.form['last_name'],'email': request.form['email']
    }
    User.create_user(data)
    return redirect('/')


@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    data = {
        'id': user_id
    }
    User.delete_user(data)
    return redirect('/')

