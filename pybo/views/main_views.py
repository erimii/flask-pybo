# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 11:41:58 2025

@author: Admin
"""


# main_views.py

from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/') 

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

























