from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
import requests
import json

def get_monographs():
    """
        A function that get all the monographs' URLs and dump them to a JSON file as:
        
        {
            `Course name (str)`: {
                `Year (int)`: `URLs (list[str])`
            }
        }
    """
    BASE_URL = "https://monografias.poli.ufrj.br/"
    CURSOS = ["Engenharia Ambiental", "Engenharia Civil", "Engenharia-Básico", "Engenharia de Computação e Informação", "Engenharia de Controle e Automação", "Engenharia de Materiais", "Engenharia de Petróleo", "Engenharia de Produção", "Engenharia Eletrônica e de Computação", "Engenharia Elétrica", "Engenharia Mecânica", "Engenharia Metalúrgica", "Engenharia Naval e Oceânica", "Engenharia Nuclear"]
    ANOS = [ano for ano in range(2003,(dt.today().year)+1)]

    font_dict = {}

    print("Starting...", end="")
    for curso in CURSOS:
        for ano in ANOS:
            print(f"\r{curso} - {ano}" + " "*20, end="")
            url = f"{BASE_URL}rel-pesquisacursoano.php?fcurso={curso}&fano={ano}"
            response = requests.get(url)
            soup = bs(response.text, "html.parser")
            monographs_links = [elem.get("href") for elem in soup.find_all("a", {"class":"linkmonografia"})]
            if len(monographs_links) == 0:
                continue
            try:
                font_dict[curso][ano] = f"{BASE_URL}{monographs_links}"
            except KeyError:
                font_dict[curso] = {}
                font_dict[curso][ano] = f"{BASE_URL}{monographs_links}"
    print("\rDone!" + " "*20)
    with open("./monographs.json", mode="w") as out:
        json.dump(font_dict, out)

if __name__ == "__main__":
    get_monographs()