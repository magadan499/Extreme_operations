from src.utils import *


# одобренные операции
approved_operations = successful_operations(get_user_operations())
# вывод пяти крайних операций
last_operations = get_last_five_operations(approved_operations)
# форматирование даты
data = formatting_date(last_operations)

# mask_card = masks_card_number()
# mask_account = masks_account_number()

print(last_operations)



