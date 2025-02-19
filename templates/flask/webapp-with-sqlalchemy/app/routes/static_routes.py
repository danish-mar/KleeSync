from flask import Blueprint, render_template

static_route_bp = Blueprint('staticroutes', __name__)


@static_route_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')
