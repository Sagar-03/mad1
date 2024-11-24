from flask import Flask, render_template, redirect, url_for, request, flash
from models import db, Admin, Customer, Professional, Service, ServiceRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///household_services.db'
app.config['SECRET_KEY'] = 'your-secret-key'
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = Admin.query.filter_by(username=username, password=password).first()
        if admin:
            return redirect(url_for('admin_dashboard'))
        flash('Invalid login credentials')
    return render_template('admin_login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    services = Service.query.all()
    return render_template('admin_dashboard.html', services=services)

# Add more routes for customers and professionals
