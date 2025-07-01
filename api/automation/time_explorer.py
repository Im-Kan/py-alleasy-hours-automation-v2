import api.automation.consts as consts

list_not_fit = [
    'Work Item does not exist, or you do not have permissions to read it',
    'Alinhamentos gerais',
    'Daily'
]
activity_types = [
    'Daily',
    'Reunião',
    'Review',
    'Refinamento'
]

def get_column_letter(ws,name):
    row = 4
    letter = ''
    for l in consts.letters:
        if ws[l+str(row)].value == name:
            letter = l
            break
    return letter
    
def add_to_dict(dict,key,value):
    cur = dict.get(key)
    if(cur is None):
        dict[key] = str(value)
    else:
        dict[key] = cur+ " | "+str(value)
def get_calendar_hashmap(ws):
    calendar_hashmap = {}
    hours_hashmap = {}
    n = 5
    while True:
        if ws['A'+n.__str__()].value is None:
            break
        date_cell = ws['A'+n.__str__()].value.__str__()[0:10].split('-')
        data = int(trim(date_cell[2]))

        title_cell = ws['B'+n.__str__()].value
        wk_type = ws[get_column_letter(ws,"Work Item Type")+n.__str__()].value.__str__()
        comment = ws[get_column_letter(ws,"Comment")+n.__str__()].value.__str__()
        activity_type = ws[get_column_letter(ws,"Activity Type")+n.__str__()].value.__str__()
        hour_cell = ws[get_column_letter(ws,"Hours")+str(n)].value
        cur_hour = hours_hashmap.get(data)
        if(cur_hour is None):
            cur_hour = 0
        hours_hashmap[data] = cur_hour + hour_cell
        if title_cell.__str__() in list_not_fit:
            n = n+1
            continue
        if activity_type == "Reunião" and comment != '':
            add_to_dict(calendar_hashmap,data,comment)
        elif activity_type in activity_types:
            add_to_dict(calendar_hashmap,data,activity_type)
        else:
            add_to_dict(calendar_hashmap,data,title_cell)
        
        n = n+1
    return (calendar_hashmap,hours_hashmap)


def trim(string):
    if string.startswith('0'):
        return string[1:]
    else:
        return string
