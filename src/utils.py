import json
from config import *
from datetime import datetime


def get_user_operations():
    """Открывает файл с операциями"""
    with open(USER_OPERATIONS, encoding="utf-8") as file:
        save_user_operations = json.load(file)
    return save_user_operations


