import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
from SharedLibrary.parser_utils import transform_data_to_dictionary, treat_value, get_string_numbers
from Classes.thesis_object import Thesis

BASE_URL = "https://monografias.poli.ufrj.br/"
CURSOS   = ["Engenharia Ambiental", "Engenharia Civil", "Engenharia-Básico", "Engenharia de Computação e Informação", "Engenharia de Controle e Automação", "Engenharia de Materiais", "Engenharia de Petróleo", "Engenharia de Produção", "Engenharia Eletrônica e de Computação", "Engenharia Elétrica", "Engenharia Mecânica", "Engenharia Metalúrgica", "Engenharia Naval e Oceânica", "Engenharia Nuclear"]
ANOS     = [ano for ano in range(1990,(dt.today().year)+1)]

def build_object(information):
    try:
        thesis_id   = get_string_numbers(information['ENDERECO'])
        title = "".join(information['TITULO'])

        print(f'[Debug] Building the object of title {title}')

        url         = information['ENDERECO']
        authors     = information['AUTORES']
        advisors    = information['ORIENTADORES']
        keywords    = information['PALAVRAS-CHAVE']
        university  = information['INSTITUICAO/CURSO'][0]
        institution = information['INSTITUICAO/CURSO'][1]
        course      = information['INSTITUICAO/CURSO'][2]
        language    = information['IDIOMA']
        year        = int("".join(information['ANO']))
        
        return Thesis(thesis_id, title, authors, advisors, url, keywords, university, institution, course, language, year)
    
    except:
        raise


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

def get_thesis_objects():
    """ For each url, gets the information and treat it 

    Returns:
        list: list of treated informations.
    """
    monographs  = get_monographs()    
    result_list = []
    
    for url in monographs:
        try:
            response = requests.get(url)
            soup = bs(response.text, "html.parser")
            monograph_data = [elem for elem in soup.find_all("td", {"valign":"top"})]

            result_list.append(build_object(treat_value(transform_data_to_dictionary(monograph_data))))
        except:
            raise

    return result_list