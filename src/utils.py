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


def clean_canselled(list_operations):
    '''Функция убирает операции в которых отсустствует ключ "date" и со статусом "CANCELLED"'''
    clean_list = []
    for i in list_operations:
        if i and i.get('date') is not None and i.get('state') == 'EXECUTED':
            clean_list.append(i)
    return clean_list


def last_operations(clean_operations):
    """
    Функция оставляет последние 5 совершенных операций
    """
    sorted_operations = sorted(clean_operations, key=lambda x: x.get('date', '0'), reverse=True)
    last_five_operations = sorted_operations[:6]
    return last_five_operations


def select_date(five_operations):
    """
    Функция переводит дату в нужный формат, удаляет пустые словари
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
