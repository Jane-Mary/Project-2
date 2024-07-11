from flask import Blueprint
from controllers.designController import index, add_design, create, view, update, delete

design = Blueprint('design', __name__)

design.route('/',methods=['GET'], strict_slashes=False)(index)
design.route('/add-design',methods=['GET'], strict_slashes=False)(add_design)
design.route('/create',methods=['POST'], strict_slashes=False)(create)
design.route('/view/<int:id>',methods=['GET'], strict_slashes=False)(view)
design.route('/update/<int:id>',methods=['GET','POST'], strict_slashes=False)(update)
design.route('/delete/<int:id>',methods=['POST','DELETE'], strict_slashes=False)(delete)