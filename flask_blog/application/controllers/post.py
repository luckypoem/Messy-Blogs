# coding: utf-8
from datetime import timedelta, date, datetime
from flask import Blueprint, render_template, redirect, request, url_for, g, \
        get_template_attribute, json, abort
from ..utils.permissions import UserPermission
from ..models import db, User, Post
from ..forms import PostForm

bp = Blueprint('post', __name__)


@bp.route('/add', methods=['GET', 'POST'])
@UserPermission()
def add():

    form = PostForm()
    if form.validate_on_submit():
        params = form.data.copy()
        post = Post(**params)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('site.index'))
    return render_template('post/add.html', form=form)
