from src.utils import *


# одобренные операции
approved_operations = successful_operations(get_user_operations())
# вывод пяти крайних операций
last_operations = get_last_five_operations(approved_operations)

for operation in last_operations:
    print(f"{format_date(operation['date'])} {operation['description']}")
    if operation['description'] == 'Перевод организации':
        print(f"{masks_card_number(operation['from'])} -> {masks_account_number(operation['to'])}")
    elif operation['description'] == 'Открытие вклада':
        print(f"{masks_account_number(operation['to'])}")
    elif operation['description'] == 'Перевод со счета на счет':
        print(f"{masks_account_number(operation['from'])} -> {masks_account_number(operation['to'])}")
    print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")
