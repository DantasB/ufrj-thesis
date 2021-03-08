import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
from unidecode import unidecode
import re

BASE_URL = "https://monografias.poli.ufrj.br/"
CURSOS   = ["Engenharia Ambiental", "Engenharia Civil", "Engenharia-Básico", "Engenharia de Computação e Informação", "Engenharia de Controle e Automação", "Engenharia de Materiais", "Engenharia de Petróleo", "Engenharia de Produção", "Engenharia Eletrônica e de Computação", "Engenharia Elétrica", "Engenharia Mecânica", "Engenharia Metalúrgica", "Engenharia Naval e Oceânica", "Engenharia Nuclear"]
ANOS     = [ano for ano in range(2003,(dt.today().year)+1)]

def get_monographs():
    """Get all the monographs' URLs.

    Returns:
        list: a list of urls.
    """
    monographs = []
    for curso in CURSOS:
        for ano in ANOS:
            print(f"[Debug] Building {curso} - {ano} " + "URL.")
            url = f"{BASE_URL}rel-pesquisacursoano.php?fcurso={curso}&fano={ano}"
            response = requests.get(url)
            soup = bs(response.text, "html.parser")
            monographs += [f"{BASE_URL}{elem.get('href')}" for elem in soup.find_all("a", {"class":"linkmonografia"})]
    
    return monographs

def treat_value(dic):
    export = {}
    for key in dic.keys():
        clean = re.compile(r",|\.|;|/(?!>)")
        if key == "endereco":
            content = unidecode(dic[key].text).replace("\n","").strip()
        else:
            content = [unidecode(elem).upper().strip() for elem in re.sub(clean, "<br/>", dic[key].decode_contents()).split("<br/>")]
        export[key] = content if len(content) > 1 else content[0]
    return export

def parse_pages():
    monographs = get_monographs()

    for url in monographs:
        try:
            response = requests.get(url)
            soup = bs(response.text, "html.parser")
            monograph_data = [elem for elem in soup.find_all("td", {"valign":"top"})]
            dic = {}
            for n in range(0,len(monograph_data),2):
                dic[unidecode(monograph_data[n].text).replace(":","").lower().strip()] = monograph_data[n+1]
        except: pass
    return dic