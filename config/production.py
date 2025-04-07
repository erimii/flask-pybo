# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 10:09:15 2025

@author: Admin
"""

from config.default import *

from dotenv import load_dotenv

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'I\xe4\xe4^\xda\xcd\x88\xcaA\x08\xc5s\xaft\xed\x18'


load_dotenv(os.path.join(BASE_DIR, '.env'))
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=os.getenv('DB_USER'),
    pw=os.getenv('DB_PASSWORD'),
    url=os.getenv('DB_HOST'),
    db=os.getenv('DB_NAME'))