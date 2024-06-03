from datetime import datetime
import json as js
import os


def open_json(path_to_file):
    """
     Получает список операций из operations.json
    """
    path_operations = os.path.abspath(path_to_file)
    with open(path_operations, 'r', encoding='utf-8') as file:
        list_operations = js.loads(file.read())
        return list_operations


def last_operations(list_operations):
    """
    Функция оставляет последние 5 операций
    """
    sorted_operations = sorted(list_operations, key=lambda x: x.get('date', '0'))
    last_five_operations = sorted_operations[:6]
    return last_five_operations


def select_date(five_operations):
    """
    Функция переводит дату в нужный формат
    """
    del five_operations[0]
    for operations in five_operations:
        operations['date'] = datetime.fromisoformat(operations['date']).strftime('%d.%m.%Y')
    return five_operations


def masc_and_split(card):
    """
    Функция забивает номер карты пробелами и маскирует его
    """
    card_number = card.split()[-1]
    if len(card_number) == 16:
        private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
        chunks, chunk_size = len(private_number), len(private_number) // 4
        masked_number = f"{card[:-len(card_number)]} {" ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)])}"
    else:
        masked_number = f'{card[:-len(card_number)]}{("**" + (card_number[-4:]))}'
    return masked_number
