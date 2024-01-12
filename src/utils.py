import json
from config import *
from datetime import datetime


def get_user_operations():
    """Открывает файл с операциями"""
    with open(USER_OPERATIONS, encoding="utf-8") as file:
        save_user_operations = json.load(file)
    return save_user_operations


def successful_operations(files):
    """Проверят операции пользователя на успешность"""
    success_operation = []
    for file in files:
        if file == {}:
            continue
        elif file['state'] == "EXECUTED":
            success_operation.append(file)
    return success_operation
