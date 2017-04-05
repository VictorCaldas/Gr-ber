from bs4 import BeautifulSoup
from openpyxl import Workbook
import requests
import datetime


def cutting_pickingup_values():
    dict_values = {}

    # Taking the information from the page
    response = requests.get("http://www.fnde.gov.br/pls/simad/internet_fnde.LIBERACOES_01_PC?p_ano=2017&p_programa"
                            "=&p_uf=SP&p_municipio=120170")

    soup = BeautifulSoup(response.text, 'html.parser')

    # Cutting information and get Values
    select_municipio = soup.find("select", attrs={"name": "p_municipio"})
    values_municipio = select_municipio.find_all("option")

    for option in values_municipio:
        ('value: {}, text: {}'.format(option['value'], option.text))
        dict_values[option['value']] = option.text

    return dict_values


def create_wb():
    wb = Workbook()  # grab the active worksheet
    ws = wb.active

    # Data can be assigned directly to cells
    ws['A1'] = 42

    # Rows can also be appended
    ws.append([1, 2, 3])

    # Python types will automatically be converted
    ws['A2'] = datetime.datetime.now()
    today = datetime.datetime.today()
    nome = 'Planilha{:02d}-{:02d}-{}.xlsx'.format(today.day, today.month, today.year)
    # Save the file
    wb.save(nome)

if __name__ == "__main__":
    cutting_pickingup_values()
    create_wb()
