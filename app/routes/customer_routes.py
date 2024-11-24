from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint('customer', __name__, url_prefix='/customer')

@bp.route('/')
@login_required
def dashboard():
    return render_template('customer/dashboard.html')

@bp.route('/request_service', methods=['GET', 'POST'])
@login_required
def request_service():
    # Handle new service request
    return render_template('customer/request_service.html')
