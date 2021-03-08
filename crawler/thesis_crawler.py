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

def parse_pages():
    """ For each url, gets the information and treat it 

    Returns:
        list: list of treated informations.
    """
    monographs  = get_monographs()    
    result_list = []
    
    for url in monographs:
        try:
            print(f'[Debug] Accessing url: {url}. ')
            response = requests.get(url)
            soup = bs(response.text, "html.parser")
            monograph_data = [elem for elem in soup.find_all("td", {"valign":"top"})]
            dic = {}
            for n in range(0,len(monograph_data),2):
                dic[unidecode(monograph_data[n].text).replace(":","").lower().strip()] = monograph_data[n+1]         
            
            print(f'[Debug] Treating informations.')
            result_list.append(treat_value(dic))
        except:
            pass

    return result_list