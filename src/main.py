import src.utils as utils


def main(path_to_json):
    list_operations = utils.open_json(path_to_json)
    clean_operations = utils.clean_canselled(list_operations)
    last_operations = utils.last_operations(clean_operations)
    sorted_operations = utils.select_date(last_operations)
    for operations in sorted_operations:
        if operations.get('from') is not None:
            masked_number_from = utils.masc_and_split(operations['from'])
            masked_number_to = utils.masc_and_split(operations['to'])
            print(f"{operations['date']} {operations['description']}\n"
                  f"{masked_number_from} -> {masked_number_to}\n"
                  f"{operations['operationAmount']['amount']} {operations['operationAmount']['currency']['name']}\n"
                  )
        else:
            print(f"{operations['date']} {operations['description']}\n"
                  f"**** -> {masked_number_to}\n"
                  f"{operations['operationAmount']['amount']} {operations['operationAmount']['currency']['name']}\n"
                  )

main('..//data/operations.json')