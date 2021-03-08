from unidecode import unidecode
import re

def remove_escaped_characters(text):
    """ Remove all escaped characters
    Args:
        text (string): the content that will have the escaped characters removed
    Returns:
        string: text without escaped characters
    """
    if (text is None):
        return
    
    # clean = re.compile(r'(\\(?:n|r|t|b|f))+')
    # return re.sub(clean, ' ', r"{}".format(text))
    return text.replace("\r\n", " ")

def clean_names(text):
    """Treats the text.

    Args:
        text (str): text to be treated

    Returns:
        str: treated text.
    """
    return unidecode(text).replace(":","").replace("/","_").replace("-","_").upper().strip()

def treat_value(informations, thesis_id):
    """ Parses the informations value and key

    Args:
        informations (dict): informations to be treated

    Returns:
        dict: treated informations
    """
    export = {
        "THESIS_ID" : int(thesis_id)
    }
    for key in informations.keys():
        clean = re.compile(r",|;|\.|/(?!>)")
        if key == "ENDERECO":
            content = unidecode(informations[key].text).replace("\n","").strip()
            export[key] = content
        else:
            if key in ["AUTORES", "ORIENTADORES"]:
                clean = re.compile(r",|;|/(?!>)")
            content = [remove_escaped_characters(unidecode(elem).upper().strip()) for elem in re.sub(clean, "<br/>", informations[key].decode_contents()).split("<br/>")]
            export[key] = list(filter(lambda i: i != "", content)) if len(content) > 1 else content[0]
    
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