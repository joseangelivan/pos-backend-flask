from flask import render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from app.models import User, PointOfSale

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        
        user = User.query.filter_by(email=email).first()
        
        if not user or not check_password_hash(user.password, password):
            flash('Credenciales incorrectas. Por favor intente nuevamente.')
            return redirect(url_for('login'))
            
        login_user(user, remember=remember)
        return redirect(url_for('dashboard'))
    
    return render_template('auth/login.html')

# Ruta de dashboard protegida
@app.route('/dashboard')
@login_required
def dashboard():
    user_pos = PointOfSale.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard/overview.html', points_of_sale=user_pos)
