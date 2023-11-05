
meses = {
    '01': "jan",
    '02': "fev",
    '03': "mar",
    '04': "abr",
    '05': "mai",
    '06': "jun",
    '07': "jul",
    '08': "ago",
    '09': "set",
    '10': "out",
    '11': "nov",
    '12': "dez"
}
meses_num = {
    1: "jan",
    2: "fev",
    3: "mar",
    4: "abr",
    5: "mai",
    6: "jun",
    7: "jul",
    8: "ago",
    9: "set",
    10: "out",
    11: "nov",
    12: "dez"
}
list_not_fit = [
    'Work Item does not exist, or you do not have permissions to read it',
    'Alinhamentos gerais',
    'Daily'

]


def obter_nome_mes(numero_mes):
    nomes_meses = [
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    ]
    nome_mes = nomes_meses[numero_mes - 1]
    return nome_mes.capitalize()
