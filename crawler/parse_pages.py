from crawler.get_monographs import get_monographs
import requests
from bs4 import BeautifulSoup as bs
from unidecode import unidecode
import re

def remove_html_tags(text):
    """ Remove all html tags
    Args:
        text (string): the content that will have the html tags removed
    Returns:
        string: text withouth html tags
    """
    if(text is None):
        return
    
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def clean_names(stg):
    return unidecode(stg).replace(":","").upper().strip()

def treat_value(dic):
    export = {}
    for key in dic.keys():
        clean = re.compile(",|\.|;|\/")
        content = [clean_names(remove_html_tags(elem)) for elem in re.sub(clean, "<br>", dic[key]).split("<br>")]
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

if __name__ == "__main__":
    print(parse_pages())