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

def clean_names(text):
    """Treats the text.

    Args:
        text (str): text to be treated

    Returns:
        str: treated text.
    """
    return unidecode(string).replace(":","").upper().strip()

def treat_value(informations):
    """ Parses the informations value and key

    Args:
        informations (dict): informations to be treated

    Returns:
        dict: treated informations
    """
    export = {}
    for key in dic.keys():
        clean = re.compile(",|\.|;|\/")
        content = [clean_names(remove_html_tags(elem)) for elem in re.sub(clean, "<br>", dic[key]).split("<br>")]
        export[key] = content if len(content) > 1 else content[0]
    
    return export

def transform_data_to_dictionary(elements):
    """Parses each element in the list and parses it in a dictionary

    Args:
        elements (list): list of html elements

    Returns:
        dictionary: treated information.
    """
    url_informations = {}
    for n in range(0,len(monograph_data),2):
        url_informations[clean_names(monograph_data[n].text)] = monograph_data[n+1]
    
    return url_informations