from flask import (
    Blueprint, redirect, jsonify, request, flash, render_template, url_for
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
        prefixedUrl = validateDestination.appendPrefix(destination)
        identical_destinations = db.getRowByDestination(prefixedUrl)
        error = None
        

        if not destination:
            error = 'URL is required'
        elif identical_destinations == 'Cannot connect to Database':
            error = 'Cannot connect to Database'

        elif type(identical_destinations) is list and len(identical_destinations) > 0:
            rootURL = request.url_root[:-1]
            forwardURL = rootURL + url_for('forwardToDestination.re', urlCode=identical_destinations[0][0])
            return jsonify(original_url=destination, new_url=forwardURL)
        
        elif validateDestination.status(destination) != 200:
            error = 'Could not connect to URL'

        if error is None:
            db.getNewUrl(prefixedUrl)
            forwardURL = request.base_url[:-3] + db.getRowByDestination(prefixedUrl)[0][0]
            return jsonify(original_url=destination, new_url=forwardURL)
        return displayError(error)

    else:
        return redirect('/')


@bp.route('/error')
def displayError(message):
    return render_template('error.html', error_message=message)