from flask import (
    Blueprint, redirect 
)

from . import db

bp = Blueprint('redirect', __name__, url_prefix='/re')

@bp.route('/<urlCode>')
def forwardToDestination(urlCode):
    try:
        destination = db.getRowByGenerated(urlCode)[0][0]
        return redirect(destination)
    except:
        return 'URL Not Found'