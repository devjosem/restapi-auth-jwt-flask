from flask import Blueprint , request , jsonify
from app.controllers.register_user import register, before_request

auth_bp = Blueprint("auth" , __name__)


auth_bp.before_request (before_request)

auth_bp.add_url_rule(
    '/users/register' , 
    view_func= register , methods = ['POST']
)
