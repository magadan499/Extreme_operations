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


def get_last_five_operations(operations):
    """Вывод пяти крайних операций"""
    sort_operations = sorted(operations, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse= True)
    return sort_operations[:5]


def format_date(value):
    """Переводим дату в необходимый формат"""
    new_data = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    return new_data


def masks_card_number(card_number):
    """Маскирует номер карты"""
    mask_number = '{} {}** **** {}'.format(card_number[: -12], card_number[-10:-8], card_number[-4:])
    return mask_number


def masks_account_number(account_number):
    """Маскирует номер счета"""
    mask_account = 'Счет **{}'.format(account_number[-4:])
    return mask_account

# print(formatting_date(get_last_five_operations(successful_operations(get_user_operations()))))
