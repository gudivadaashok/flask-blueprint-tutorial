"""General page routes."""
from flask import Blueprint, render_template
from flask import current_app as app
from application.api import fetch_products

# Blueprint Configuration
home_bp = Blueprint('home_bp', __name__,
                    template_folder='templates',
                    static_folder='static', url_prefix='')


@home_bp.route('/', methods=['GET'])
def home():
    """Homepage."""
    products = fetch_products(app)
    return render_template('index.jinja2',
                           title='Flask Blueprint Tutorial',
                           subtitle='My Fake Ecommerce Store',
                           template='home-template',
                           products=products)


@home_bp.route('/about', methods=['GET'])
def about():
    """About page."""
    return render_template('index.jinja2',
                           title="About",
                           subtitle='This is an example about page.',
                           template='home-template page')


@home_bp.route('/contact', methods=['GET'])
def contact():
    """Contact page."""
    return render_template('index.jinja2',
                           title="Contact",
                           subtitle='This is an example contact page.',
                           template='home-template page')
