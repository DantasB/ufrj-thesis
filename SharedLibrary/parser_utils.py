from unidecode import unidecode
import re

def get_string_numbers(information):
    """gets the information digits

    Args:
        information (str): url with a number at the end.

    Returns:
        int: integers in the information string
    """
    result = re.findall('[0-9]+', information)
    return int("".join(result))

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

def change_information_content(key, content):
    """ Strip the information to get just the html content

    Args:
        key (str): dictionary key
        content (str): content to be treated

    Returns:
        str: treated content
    """
    clean = re.compile(r",|\.|;|/(?!>)")
    if key == "ENDERECO":
        content = unidecode(content.text).replace("\n","").strip()
    else:
        content = [unidecode(elem).upper().strip() for elem in re.sub(clean, "<br/>", content.decode_contents()).split("<br/>")]
    
    return content

def treat_value(informations):
    """ Parses the informations value and key

    Args:
        informations (dict): informations to be treated

    Returns:
        dict: treated informations
    """
    export = {}
    for key in informations.keys():
        export[key] = change_information_content(key, informations[key])
    
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