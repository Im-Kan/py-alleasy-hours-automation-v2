

list_not_fit = [
    'Work Item does not exist, or you do not have permissions to read it',
    'Alinhamentos gerais',
    'Daily'
]


def get_calendar_hashmap(ws):
    calendar_hashmap = {}
    n = 5
    while True:
        if ws['A'+n.__str__()].value is None:
            break
        date_cell = ws['A'+n.__str__()].value.__str__()[0:10].split('-')
        data = int(trim(date_cell[2]))

        title_cell = ws['B'+n.__str__()].value
        if title_cell.__str__() in list_not_fit:
            n = n+1
            continue
        cur = calendar_hashmap.get(data)
        if cur is None:
            calendar_hashmap[data] = title_cell
        else:
            calendar_hashmap[data] = cur + " | " + title_cell
        n = n+1
    return calendar_hashmap


def trim(string):
    if string.startswith('0'):
        return string[1:]
    else:
        return string
