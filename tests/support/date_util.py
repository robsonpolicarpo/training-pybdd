import re
from datetime import datetime, timedelta


def date_by_test(param: str, formato='%d/%m/%Y'):
    if param.upper() == 'D':
        return datetime.now().__format__(formato)
    else:
        days = re.search('\\d+', param).group()
        if param.__contains__('+'):
            return date_plus(int(days), formato)
        else:
            return date_minus(int(days), formato)


def date_plus(days: int, dt_format='%d/%m/%Y'):
    date = datetime.now() + timedelta(days=days)
    return date.__format__(dt_format)


def date_minus(days: int, dt_format='%d/%m/%Y'):
    date = datetime.now() - timedelta(days=days)
    return date.__format__(dt_format)
