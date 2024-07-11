from flask import Blueprint
from controllers.homeController import homes, liv, din, kit, bed

home = Blueprint('home', __name__)

home.route('/',methods=['GET'], strict_slashes=False)(homes)
home.route('/liv',methods=['GET'], strict_slashes=False)(liv)
home.route('/din',methods=['GET'], strict_slashes=False)(din)
home.route('/kit',methods=['GET'], strict_slashes=False)(kit)
home.route('/bed',methods=['GET'], strict_slashes=False)(bed)
