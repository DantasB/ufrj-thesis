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
    return unidecode(text).replace(":","").upper().strip()

def treat_value(informations):
    """ Parses the informations value and key

    Args:
        informations (dict): informations to be treated

    Returns:
        dict: treated informations
    """
    export = {}
    for key in informations.keys():
        clean = re.compile(r",|\.|;|/(?!>)")
        if key == "endereco":
            content = unidecode(informations[key].text).replace("\n","").strip()
        else:
            content = [unidecode(elem).upper().strip() for elem in re.sub(clean, "<br/>", informations[key].decode_contents()).split("<br/>")]
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
    for n in range(0,len(elements),2):
        url_informations[clean_names(elements[n].text)] = elements[n+1]
    
    return url_informations