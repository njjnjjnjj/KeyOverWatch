__version__ = '0.0.1'
__author__ = 'njjnjjnjj'

import os

# 定义项目的根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_SQL_DIR = os.path.join(STATIC_DIR, 'sql')
STATIC_IMAGE_DIR = os.path.join(STATIC_DIR, 'images')