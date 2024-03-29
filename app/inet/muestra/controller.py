from flask import Blueprint
from flask import render_template

from .model import Muestra

bp = Blueprint('muestra', __name__)

@bp.route('/')
def index():
    data = Muestra.query.order_by(Muestra.id.desc()).all()[:144]
    intensities = [d.i for d in data]
    intensities.reverse()
    return render_template('index.html', data=data, intensities=intensities)
