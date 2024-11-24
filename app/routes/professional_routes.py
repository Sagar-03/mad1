from flask import Blueprint, render_template
from flask_login import login_required, current_user

bp = Blueprint('professional', __name__, url_prefix='/professional')

@bp.route('/')
@login_required
def dashboard():
    return render_template('professional/dashboard.html')

@bp.route('/requests')
@login_required
def view_requests():
    # Show assigned service requests
    return render_template('professional/requests.html')
