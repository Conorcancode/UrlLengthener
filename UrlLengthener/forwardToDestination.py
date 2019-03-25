from flask import (
    Blueprint, redirect, jsonify, request, flash
)
from . import db
from . import validateDestination

bp = Blueprint('forwardToDestination', __name__, url_prefix='/api/shorturl')

@bp.route('/<urlCode>')
def re(urlCode):
    try:
        destination = db.getRowByGenerated(urlCode)

        return redirect(destination[0][0])
    except:
        return 'URL Not Found'

@bp.route('/new', methods=('GET', 'POST'))
def displayJSON():

    if request.method == 'POST':
        destination = request.form['destination']
        identical_destinations = db.getRowByDestination(destination)
        error = None

        if not destination:
            error = 'URL is required'
        elif identical_destinations == 'Cannot connect to Database':
            error = 'Cannot connect to Database'
        
        elif validateDestination.status(destination) != 200:
            error = 'Could not connect to URL'

        elif type(identical_destinations) is list and len(identical_destinations) > 0:

            return jsonify(original_url=destination, new_url=identical_destinations[0][0])
        
        if error is None:
            db.getNewUrl(destination)
            forwardURL = db.getRowByDestination(destination)[0][0]
            return jsonify(original_url=destination, new_url=forwardURL)
        return error
        flash(error)
