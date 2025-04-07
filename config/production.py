# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 10:09:15 2025

@author: Admin
"""

from config.default import *

from dotenv import load_dotenv

load_dotenv(os.path.join(BASE_DIR, '.env'))
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=os.getenv('DB_USER'),
    pw=os.getenv('DB_PASSWORD'),
    url=os.getenv('DB_HOST'),
    db=os.getenv('DB_NAME'))