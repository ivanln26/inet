from flask import Blueprint
from flask import render_template

from .models import Muestra

bp = Blueprint('muestra', __name__)

@bp.route('/')
def index():
    data = Muestra.query.order_by(Muestra.id.desc()).all()[:144]
    return render_template('index.html', data=data)
