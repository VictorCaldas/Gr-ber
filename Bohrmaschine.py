import re
from bs4 import BeautifulSoup
from openpyxl import Workbook
import requests
import datetime


def cutting_pickingup_values():
    dict_values = {}

    # Taking the information from the page
    response = requests.get("http://www.fnde.gov.br/pls/simad/internet_fnde.LIBERACOES_01_PC?p_ano=2017&p_programa=&p_uf=SP&p_municipio=120170")

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
    li =[['Entidade..: 44.518.405/0001-91 - PREF MUN DE ALVINLANDIA'], ['Município.: ALVINLANDIA - SP'], ['ALIMENTAÇÃO ESCOLAR - PROG.NACIONAL DE ALIMENTAÇÃO ESCOLAR'], ['Data Pgto'], ['OB'], ['Valor'], ['Programa'], ['Banco'], ['Agência'], ['C/C'], ['08/MAR/2017'], ['802989'], ['212,00'], ['PNAE - Alimentação Escolar - AEE'], ['BANCO DO BRASIL'], ['6877'], ['0000169374'], ['08/MAR/2017'], ['802990'], ['454,40'], ['PNAE - Alimentação Escolar - EJA'], ['BANCO DO BRASIL'], ['6877'], ['0000169374'], ['08/MAR/2017'], ['802991'], ['979,20'], ['PNAE - Alimentação Escolar - Ensino Médio'], ['BANCO DO BRASIL'], ['6877'], ['0000169374'], ['14/MAR/2017'], ['803132'], ['2.610,80'], ['PNAE - Alimentação Escolar - Creche'], ['BANCO DO BRASIL'], ['6877'], ['0000169374'], ['14/MAR/2017'], ['803140'], ['3.168,00'], ['PNAE - Alimentação Escolar -Ensino Fundamental'], ['BANCO DO BRASIL'], ['6877'], ['0000169374'], ['14/MAR/2017'], ['803145'], ['1.267,40'], ['PNAE - Alimentação Escolar - Pré-escola.'], ['BANCO DO BRASIL'], ['6877'], ['0000169374'], ['05/ABR/2017'], ['804810'], ['3.168,00'], ['PNAE - Alimentação Escolar -Ensino Fundamental'], ['BANCO DO BRASIL'], ['6877'], ['0000169374'], ['05/ABR/2017'], ['804815'], ['979,20'], ['PNAE - Alimentação Escolar - Ensino Médio'], ['BANCO DO BRASIL'], ['6877'], ['0000169374'], ['05/ABR/2017'], ['804835'], ['454,40'], ['PNAE - Alimentação Escolar - EJA'], ['BANCO DO BRASIL'], ['6877'], ['0000169374'], ['05/ABR/2017'], ['804839'], ['212,00'], ['PNAE - Alimentação Escolar - AEE'], ['BANCO DO BRASIL'], ['6877'], ['0000169374'], ['05/ABR/2017'], ['805005'], ['1.267,40'], ['PNAE - Alimentação Escolar - Pré-escola.'], ['BANCO DO BRASIL'], ['6877'], ['0000169374'], ['05/ABR/2017'], ['805040'], ['2.610,80'], ['PNAE - Alimentação Escolar - Creche'], ['BANCO DO BRASIL'], ['6877'], ['0000169374'], ['07/ABR/2017'], ['805165'], ['4.160,60'], ['MAIS EDUCAÇÃO - Fundamental'], ['BANCO DO BRASIL'], ['6877'], ['0000169374'], ['Total:'], ['21.544,20'], ['']]


    today = datetime.datetime.today()
    nome = 'Planilha{:02d}-{:02d}-{}.xlsx'.format(today.day, today.month, today.year)
    # Save the file
    for row, val in enumerate(li, start=1):
        if val == "Entidade":
            print("achou")
        ws.cell(row=row, column=1).value = val

    wb.save(nome)

if __name__ == "__main__":
    cutting_pickingup_values()
    create_wb()
