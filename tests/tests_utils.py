from src.utils import *



def test_successful_operations():
    """Проверяем функцию успешных операций"""
    assert successful_operations([{}]) == []
    assert successful_operations([{"state": "EXECUTED"}]) == [{"state": "EXECUTED"}]
