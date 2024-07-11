from flask import render_template
from model.designModel import Designs


def homes():
    return render_template('home.html' ,title='Home')


def liv():
     design = Designs.query.all() 
     return render_template('liv.html',design=design ,title='Living')
 
def din():
    return render_template('din.html', title='Dinning')

def kit():
    return render_template('kit.html', title='Kitchen')

def bed():
    return render_template('bed.html' ,title='Bedroom')

