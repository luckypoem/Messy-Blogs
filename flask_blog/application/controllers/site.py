# coding: utf-8
from flask import render_template, Blueprint
from ..models import Post
bp = Blueprint('site', __name__)


@bp.route('/')
def index():
    """Index page."""
    posts_data = Post.query.all()
    return render_template('site/index.html', posts_data=posts_data)


@bp.route('/about')
def about():
    """About page."""
    return render_template('site/about.html')
