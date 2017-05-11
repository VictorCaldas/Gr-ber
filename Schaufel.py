import requests
import time
import datetime
from bs4 import BeautifulSoup
from money import Money
from openpyxl import Workbook


def cutting_pickingup_values():
    dict_values = {}

    # Taking the information from the page
    response = requests.get("http://www.fnde.gov.br/pls/simad/internet_fnde.LIBERACOES_01_PC?p_ano=2017&p_programa"
                            "=&p_uf=SP&p_municipio "
                            "=120170")

    soup = BeautifulSoup(response.text, 'html.parser')

    # Cutting information and get Values
    select_municipio = soup.find("select", attrs={"name": "p_municipio"})
    values_municipio = select_municipio.find_all("option")

    for option in values_municipio:
        ('value: {}, text: {}'.format(option['value'], option.text))
        dict_values[option['value']] = option.text

    return dict_values


def report_fnde():
    delay = 0
    control = 0

    # get cookies
    mySession = requests.session()
    mySession.get("http://www.fnde.gov.br/pls/simad/internet_fnde.liberacoes_01_pc")

    # Get values for all places
    dict_values = cutting_pickingup_values()
    li = []
    for key in dict_values.keys():
        data = [
            ('p_ano', '2017'),
            ('p_verifica', 'sigef'),
            ('p_programa', 'C7'),
            ('p_cgc', ''),
            ('p_uf', 'SP'),
            ('p_municipio', key),
            ('p_tp_entidade', '02'),
        ]

        # Create preview
        preview = mySession.post('http://www.fnde.gov.br/pls/simad/internet_fnde.liberacoes_result_pc', data=data)
        a = open("preview.html", "w")
        a.write(preview.text)
        a.close()

        # Magic Baby
        soup = BeautifulSoup(preview.text, 'html.parser')
        alltables = soup.findAll("table", attrs={"border": "1", "width": "100%"})

        # excell - failed :(
        wb = Workbook()  # grab the active worksheet
        ws = wb.active
        today = datetime.datetime.today()
        nome = 'Planilha{:02d}-{:02d}-{}.xlsx'.format(today.day, today.month, today.year)

        for table in alltables:
            rows = table.findAll('tr')
            for tr in rows:
                cols = tr.findAll('td')
                print("   ")
                for td in cols:
                    print(td.text.strip(), end='\t' * 3)
                    li.append(td.text.strip())
                    if control == 1:
                        value = td.text.strip().replace(".", "").replace(",", ".")
                        value = float(value)
                        a = value * 10
                        b = a * 30
                        value_agricultura_familiar = b / 100
                        print('\n')
                        print("Total 2017: ")
                        value_total_2017 = Money(a, 'BRL')
                        print(str(value_total_2017).replace("BRL", "R$"))
                        li.append("Total 2017: ")
                        li.append(value_total_2017)
                        print('\n')
                        print("Agricultura Familiar: ")
                        li.append("Agricultura Familiar: ")
                        li.append(value_agricultura_familiar)
                        print(str(Money(value_agricultura_familiar, 'BRL')).replace("BRL", "R$"))
                        control = 0
                    if td.text.strip() == "Total:":
                        control = 1
        print('\n'"-----------------------------------------------------------------------------")
        time.sleep(delay)
    print('\n'"Fim do Relatório")

    # wb.save(nome)
    # for i in li:
    # print(i)


if __name__ == "__main__":
    report_fnde()
