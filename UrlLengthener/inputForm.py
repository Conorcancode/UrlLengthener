from flask import (
    Blueprint, render_template, request, flash, redirect, url_for, jsonify
)
from . import db

bp = Blueprint('inputForm', __name__, url_prefix='/')

@bp.route('/', methods=('GET', 'POST'))
def submitURL():
    if request.method == 'POST':
        destination = request.form['destination']
        redirectURL = request.url_root + 'api/shorturl/'
        identical_destinations = db.getRowByDestination(destination)
        error = None

        if not destination:
            error = 'URL is required'
        elif identical_destinations == 'Cannot connect to Database':
            error = 'Cannot connect to Database'
        elif type(identical_destinations) is list and len(identical_destinations) > 0:
            redirectURL += identical_destinations[0][0]
            return jsonify(original_url=destination, short_url=redirectURL)
        
        if error is None:
            db.getNewUrl(destination)
            forwardURL = redirectURL + db.getRowByDestination(destination)[0][0]
            return jsonify(original_url=destination, short_url=forwardURL)
        
        flash(error)
    
    return render_template('index.html')
