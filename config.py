# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 09:18:15 2025

@author: Admin
"""

import os

BASE_DIR = os.path.dirname(__file__)

# db 접속 주소
# SQLite db가 사용되고 db 파일은 프로젝트 홈 디렉터리 바로 밑에 pybo.db 파일로 저장
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))

# 이벤트 처리 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False

