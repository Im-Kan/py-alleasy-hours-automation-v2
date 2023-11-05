from openpyxl.styles import PatternFill
from datetime import time


def set_data(ws, mes, ano, dias_no_mes):
    ws['B4'].value = "01/"+mes.__str__()+"/"+ano.__str__()
    ws['E4'].value = dias_no_mes.__str__()+"/"+mes.__str__()+"/"+ano.__str__()


def set_horas(ws, calendar_hashmap, dias_do_mes):
    n = 10
    for dia in range(1, dias_do_mes+1):
        n = n+1
        obs = calendar_hashmap.get(dia)
        if obs is None:
            fill_empty(ws, n, obs)
            continue
        fill_work(ws, n, obs)
        print(n, ' ', dia, "=>", obs)


def fill_work(ws, n, obs):
    fill_white(ws, n, obs)
    hora = time(8, 0, 0)
    ws.row_dimensions[n].height = 30
    ws['P'+n.__str__()].value = obs
    ws['E'+n.__str__()].value = "09:00:00"
    ws['F'+n.__str__()].value = "12:00:00"
    ws['G'+n.__str__()].value = "13:00:00"
    ws['H'+n.__str__()].value = "18:00:00"
    ws['K'+n.__str__()].value = hora
    ws['M'+n.__str__()].value = hora


def fill_empty(ws, n, obs):
    gray = "C0C0C0"
    empty_filler = PatternFill(start_color=gray, end_color=gray, fill_type="solid")

    ws['A'+n.__str__()].fill = empty_filler
    ws['B'+n.__str__()].fill = empty_filler
    ws['C'+n.__str__()].fill = empty_filler
    ws['D'+n.__str__()].fill = empty_filler
    ws['E'+n.__str__()].fill = empty_filler
    ws['F'+n.__str__()].fill = empty_filler
    ws['G'+n.__str__()].fill = empty_filler
    ws['H'+n.__str__()].fill = empty_filler
    ws['I'+n.__str__()].fill = empty_filler
    ws['J'+n.__str__()].fill = empty_filler
    ws['K'+n.__str__()].fill = empty_filler
    ws['L'+n.__str__()].fill = empty_filler
    ws['M'+n.__str__()].fill = empty_filler
    ws['P'+n.__str__()].fill = empty_filler


def fill_white(ws, n, obs):
    color = "ffffff"
    empty_filler = PatternFill(start_color=color, end_color=color, fill_type="solid")
    ws['A'+n.__str__()].fill = empty_filler
    ws['B'+n.__str__()].fill = empty_filler
    ws['C'+n.__str__()].fill = empty_filler
    ws['D'+n.__str__()].fill = empty_filler
    ws['E'+n.__str__()].fill = empty_filler
    ws['F'+n.__str__()].fill = empty_filler
    ws['G'+n.__str__()].fill = empty_filler
    ws['H'+n.__str__()].fill = empty_filler
    ws['I'+n.__str__()].fill = empty_filler
    ws['J'+n.__str__()].fill = empty_filler
    ws['K'+n.__str__()].fill = empty_filler
    ws['L'+n.__str__()].fill = empty_filler
    ws['M'+n.__str__()].fill = empty_filler
    ws['P'+n.__str__()].fill = empty_filler
    # while True:
    #     dia = ws['B'+n.__str__()].value.__str__()
    #     if dia is None:
    #         break
    #
    #     print("diaa", dia)
    #     obs = calendar_hashmap[dia]
    #     ws['P'+n.__str__()].value = obs
    #     print(dia, "=>", obs)
