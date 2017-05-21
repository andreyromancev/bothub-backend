import os
import sys
from lib.framework.celeryapp import app as celery_app

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
__all__ = ['celery_app']


def append_path(path):
    if path not in sys.path:
        sys.path.append(path)


append_path(os.path.join(BASE_DIR, 'service'))

