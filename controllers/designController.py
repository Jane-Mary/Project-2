from flask import render_template, request, redirect
from config import db
from model.authModel import Users
from model.designModel import Designs


def index():
    design = Designs.query.all() 
    users = Users.query.all()
    return render_template('home.html', title= 'Home Page',design=design)



def add_design(): 
     return render_template('add-task.html', title='Add New Task')


def create():
     form = request.form
     name = form['name']
     price = form['price']
     location = form['location']
     image = form ['image']
     description = form['description']

     designs = Designs(name=name, price=price,image=image, description=description, location=location)
     db.session.add(designs)
     db.session.commit()

     return redirect('/')


def view(id):
     designs = Designs.query.get(id)

     return render_template('view.html',title='Details Page', designs=designs)



def update(id):
      designs = Designs.query.filter_by(id = id).first()
      if designs is None:
           return redirect('/')
      if request.method == 'GET':
           return render_template('update.html',designs=designs)
      elif request.method == 'POST':
          form = request.form
          title = form['title']
          description = form['description']
          leader = form['leader']

          designs.title= title
          designs.description = description
          designs.leader = leader

          db.session.commit() 
          return redirect('/')
      return render_template('update.html', title= 'Edit Task', designs=designs) 



def delete(id):
     if request.method == 'POST' :
          if request.form['_method'] == 'DELETE':
               article = Designs.query.get(id)
               db.session.delete(article)
               db.session.commit()
               return redirect('/')