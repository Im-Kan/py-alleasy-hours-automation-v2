from openpyxl import load_workbook
from glob import glob
import api.automation.time_explorer as time_explorer
import api.automation.alleasy as alleasy
import calendar
import base64
from io import BytesIO


def generateAlleasyExcel(data):
    mes = int(data["date"].split("/")[0])
    ano = int(data["date"].split("/")[1])
    _, dias_no_mes = calendar.monthrange(ano, mes)

    # devops_file = glob("./time_explorer_excel/*.xlsx")[0]
    decrypted = base64.b64decode(data["base64"])
    devops_file = BytesIO(decrypted)
    wk_devops = load_workbook(devops_file)
    ws_devops = wk_devops.active

    alleasy_file = glob("./api/automation/alleasy_model_excel/*.xlsx")[0]
    wk_alleasy = load_workbook(alleasy_file)
    ws_alleasy = wk_alleasy.active

    (calendar_te,hour_hashmap) = time_explorer.get_calendar_hashmap(ws_devops)

    alleasy.set_data(ws_alleasy, mes, ano, dias_no_mes)
    alleasy.set_horas(ws_alleasy, calendar_te, dias_no_mes,hour_hashmap)
    alleasy.set_nome(ws_alleasy, data["name"])

    bytes_io = BytesIO()

    wk_alleasy.save(bytes_io)
    bytes_data = bytes_io.getvalue()
# Encode the bytes using base64
    base64_data = base64.b64encode(bytes_data).decode('utf-8')
    return base64_data
