from bs4 import BeautifulSoup
import requests

# Taking the information from the page
response = requests.get("http://www.fnde.gov.br/pls/simad/internet_fnde.LIBERACOES_01_PC?p_ano=2017&p_programa=&p_uf"
                        "=SP&p_municipio=120170")

# Soup Action
soup = BeautifulSoup(response.text, 'html.parser')

# Cutting information and get Values
select_municipio = soup.find("select", attrs={"name":"p_municipio"})
values_municipio = select_municipio.find_all("option")

for option in values_municipio:
    print ('value: {}, text: {}'.format(option['value'], option.text))
