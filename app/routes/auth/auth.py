from flask import Blueprint
from app.controllers.register_user import register

auth_bp = Blueprint("auth" , __name__)

auth_bp.add_url_rule(

    '/users/register' , 
    view_func= register , methods = ['POST']
)
