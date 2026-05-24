from flask import Blueprint

auth_bp = Blueprint("auth" , __name__)


@auth_bp.route("/users/register")

@auth_bp.user("/users/login")