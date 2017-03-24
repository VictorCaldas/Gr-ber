import requests

mySession = requests.session()
mySession.get("http://www.fnde.gov.br/pls/simad/internet_fnde.liberacoes_01_pc")

headers = {
    'Origin': 'http://www.fnde.gov.br',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.6,en;q=0.4',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'http://www.fnde.gov.br/pls/simad/internet_fnde.LIBERACOES_01_PC?p_ano=2017&p_programa=C7&p_uf=SP&p_municipio=120170',
    'Connection': 'keep-alive',
}

data = [
  ('p_ano', '2017'),
  ('p_verifica', 'sigef'),
  ('p_programa', 'C7'),
  ('p_cgc', ''),
  ('p_uf', 'SP'),
  ('p_municipio', '350010'),
  ('p_tp_entidade', '02'),
]

preview = mySession.post('http://www.fnde.gov.br/pls/simad/internet_fnde.liberacoes_result_pc', headers=headers, data=data)
a = open("preview.html","w")
a.write(preview.text)
a.close()