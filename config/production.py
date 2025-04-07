# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 10:09:15 2025

@author: Admin
"""

from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'I\xe4\xe4^\xda\xcd\x88\xcaA\x08\xc5s\xaft\xed\x18'
