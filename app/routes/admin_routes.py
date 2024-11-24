from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from ..models import Service, ServiceRequest, User
from .. import db

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/')
@login_required
def dashboard():
    return render_template('admin/dashboard.html')

@bp.route('/add_service', methods=['GET', 'POST'])
@login_required
def add_service():
    # Handle service addition
    return render_template('admin/add_service.html')

@bp.route('/manage_users')
@login_required
def manage_users():
    # Manage and block/unblock users
    return render_template('admin/manage_users.html')
