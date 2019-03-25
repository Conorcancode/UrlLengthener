from flask import (
    Blueprint, render_template, request, flash
)
from . import db
from . import forwardToDestination

bp = Blueprint('inputForm', __name__, url_prefix='/')

@bp.route('/', methods=('GET', 'POST'))
def submitURL():
    return render_template('index.html')
