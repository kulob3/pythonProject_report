from src.utils import open_json, clean_canselled, last_operations, select_date, masc_and_split


def test_open_json():
    assert open_json('test_json.json') == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }, {}
    ]


def test_clean_cansalled():
    assert clean_canselled([
        {"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
        {"state": "CANCELLED", "date": "2019-08-26T10:50:58.294041"},
        {"state": "EXECUTED"}
    ]) == [
        {"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"}
    ]


def test_last_operations():
    assert last_operations([
        {"date": "2020-08-26T10:50:58.294041"},
        {"date": "2019-08-26T10:50:58.294041"},
        {"date": "2019-08-27T10:50:58.294041"}
    ]) == [
         {"date": "2020-08-26T10:50:58.294041"},
         {"date": "2019-08-27T10:50:58.294041"},
         {"date": "2019-08-26T10:50:58.294041"}
    ]


def test_select_date():
    assert select_date([{}, {"date": "2019-08-27T10:50:58.294041"}, {"date": "2020-08-26T10:50:58.294041"},]) == [{"date": "27.08.2019"}, {"date": "26.08.2020"}]


def test_masc_and_split():
    assert masc_and_split("Maestro 1596837868705199") == "Maestro  1596 83** **** 5199"
    assert masc_and_split("Счет 64686473678894779589") == "Счет **9589"
