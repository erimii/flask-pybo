# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 10:08:54 2025

@author: Admin
"""

from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"
