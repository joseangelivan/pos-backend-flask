from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app import db
from app.main import bp
from app.models import PointOfSale
from app.main.forms import PointOfSaleForm

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('main/index.html', title='Inicio')

@bp.route('/dashboard')
@login_required
def dashboard():
    points_of_sale = current_user.points_of_sale.all()
    return render_template('main/dashboard.html', 
                         title='Dashboard',
                         points_of_sale=points_of_sale)

@bp.route('/pos/new', methods=['GET', 'POST'])
@login_required
def create_pos():
    form = PointOfSaleForm()
    if form.validate_on_submit():
        pos = PointOfSale(
            name=form.name.data,
            location=form.location.data,
            address=form.address.data,
            phone=form.phone.data,
            owner=current_user
        )
        db.session.add(pos)
        db.session.commit()
        flash('Punto de venta creado exitosamente!', 'success')
        return redirect(url_for('main.dashboard'))
    
    return render_template('main/create_pos.html', 
                         title='Nuevo Punto de Venta',
                         form=form)

@bp.route('/pos/<int:id>')
@login_required
def view_pos(id):
    pos = PointOfSale.query.get_or_404(id)
    if pos.owner != current_user and not current_user.is_admin:
        flash('No tienes permiso para ver este punto de venta', 'danger')
        return redirect(url_for('main.dashboard'))
    
    return render_template('main/view_pos.html', 
                         title=pos.name,
                         pos=pos)
