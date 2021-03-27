import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
from SharedLibrary.parser_utils import transform_data_to_dictionary, treat_value
from Classes.thesis_object import Thesis

BASE_URL = "https://monografias.poli.ufrj.br/"
ANOS = [ano for ano in range(1990, (dt.today().year)+1)]
CURSOS = ["Engenharia Ambiental", "Engenharia Civil", "Engenharia de Computação e Informação", "Engenharia de Controle e Automação", "Engenharia de Materiais", "Engenharia de Petróleo",
          "Engenharia de Produção", "Engenharia Eletrônica e de Computação", "Engenharia Elétrica", "Engenharia Mecânica", "Engenharia Metalúrgica", "Engenharia Naval e Oceânica", "Engenharia Nuclear"]


def build_object(information, thesis_id):
    try:
        title = "".join(information['TITULO'])

        print(f'[Debug] Building the object of title {title}')

        url = information['ENDERECO']
        authors = information['AUTORES']
        advisors = information['ORIENTADORES']
        keywords = information['PALAVRAS_CHAVE']
        university = information['INSTITUICAO_CURSO'][0]
        institution = information['INSTITUICAO_CURSO'][1]
        course = information['INSTITUICAO_CURSO'][2]
        language = information['IDIOMA']
        year = int("".join(information['ANO']))

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
        print(f"[Debug] Building {curso} thesis " + "URLs.")
        url = f"{BASE_URL}rel-pesquisacurso.php?fcurso={curso}"
        response = requests.get(url)
        soup = bs(response.text, "html.parser")
        monographs += [f"{BASE_URL}{elem.get('href')}" for elem in soup.find_all("a", {
            "class": "linkmonografia"})]

    return monographs


def get_thesis_objects(THESIS_IDS):
    """ For each url, gets the information and treat it 

    Returns:
        list: list of treated informations.
    """
    monographs = get_monographs()
    result_list = []

    for url in monographs:
        try:
            thesis_id = int(url[url.rfind("fcodigo=")+8:])
            if thesis_id in THESIS_IDS:
                continue

            response = requests.get(url)
            soup = bs(response.text, "html.parser")
            monograph_data = [elem for elem in soup.find_all(
                "td", {"valign": "top"})]

            result_list.append(build_object(treat_value(
                transform_data_to_dictionary(monograph_data)), thesis_id))
        except:
            raise

    return result_list
