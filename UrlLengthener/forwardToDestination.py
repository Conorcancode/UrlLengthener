from flask import (
    Blueprint, redirect 
)

from . import db

bp = Blueprint('forwardToDestination', __name__, url_prefix='/re')

@bp.route('/<urlCode>')
def re(urlCode):
    try:
        destination = db.getRowByGenerated(urlCode)

        return redirect(destination[0][0])
    except:
        return 'URL Not Found'