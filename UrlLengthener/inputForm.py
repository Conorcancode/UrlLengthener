from flask import (
    Blueprint, render_template, request, flash, redirect, url_for
)
from . import db

bp = Blueprint('inputForm', __name__, url_prefix='/')

@bp.route('/', methods=('GET', 'POST'))
def submitURL():
    if request.method == 'POST':
        destination = request.form['destination']

        identical_destinations = db.getRowByDestination(destination)
        error = None

        if not destination:
            error = 'URL is required'
        elif identical_destinations == 'Cannot connect to Database':
            error = 'Cannot connect to Database'
        elif type(identical_destinations) is list and len(identical_destinations) > 0:
            error = 'Redirect already exists'
        
        if error is None:
            db.getNewUrl(destination)
            forwardURL = db.getRowByDestination(destination)[0][0]
            return redirect(url_for('inputForm.result', generated_path = forwardURL))
        
        flash(error)
    
    return render_template('index.html')

@bp.route('/result')
def result():

    return render_template('result.html')