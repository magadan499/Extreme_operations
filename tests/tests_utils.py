import pytest
from src.utils import *


def test_successful_operations():
    """Проверяем функцию успешных операций"""
    assert successful_operations([{}]) == []
    assert successful_operations([{"state": "EXECUTED"}]) == [{"state": "EXECUTED"}]


def test_get_last_five_operations():
    """Проверка вывода пяти крайних операций по дате"""
    assert get_last_five_operations([{"date": "2019-08-26T10:50:58.294041"},
                                     {"date": "2019-07-03T18:35:29.512364"},
                                     {"date": "2018-06-30T02:08:58.425572"},
                                     {"date": "2018-03-23T10:45:06.972075"},
                                     {"date": "2019-04-04T23:20:05.206878"},
                                     {"date": "2019-03-23T01:09:46.296404"}]) == [{'date': '2019-08-26T10:50:58.294041'},
                                                                                  {'date': '2019-07-03T18:35:29.512364'},
                                                                                  {'date': '2019-04-04T23:20:05.206878'},
                                                                                  {'date': '2019-03-23T01:09:46.296404'},
                                                                                  {'date': '2018-06-30T02:08:58.425572'}]


def test_formatting_date():
    """Проверка форматирования даты"""
    assert formatting_date([{"date": "2024-01-12T10:50:58.294041"}]) == ["12.01.2024"]


def test_masks_card_number():
    """Проверка маскировки карты"""
    assert masks_card_number('4598300720424501') == '4598 07** **** 4501'


def test_masks_account_number():
    """Проверка маскировки счета"""
    assert masks_account_number('Счет 43597928997568165086') == 'Счет **5086'
