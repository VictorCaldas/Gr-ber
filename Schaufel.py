import requests
import time
from bs4 import BeautifulSoup
from Bohrmaschine import cutting_pickingup_values

TIME = 0

# get cookies
mySession = requests.session()
mySession.get("http://www.fnde.gov.br/pls/simad/internet_fnde.liberacoes_01_pc")

# Get values for all places
dict_values = cutting_pickingup_values()

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

    for table in alltables:
        rows = table.findAll('tr')
        for tr in rows:
            cols = tr.findAll('td')
            print("   ")
            for td in cols:
                print(td.text.strip(), end='\t'*3)

    print('\n'"---------------------------------------------------------------")
    time.sleep(TIME)
print('\n'"Fim do Relatório")