from decimal import Decimal


def str_to_decimal(str_value: str):
    str_value = str_value.replace('.', '').replace(',', '.').strip('R$ ')
    return Decimal(str_value)
