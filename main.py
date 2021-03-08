import os

from Classes.thesis_object import Thesis
from crawler.thesis_crawler import parse_pages
from SharedLibrary import mongo_utils
from flask import jsonify
from dotenv import load_dotenv, find_dotenv

def load_parameters():
    """ Loads all .env parameters.

    Returns:
        dictionary: an object with the .env informations.
    """
    load_dotenv(find_dotenv())
    try:
        return {"connection_url" : os.environ.get("CONNECTION_URL"),
                "username" : os.environ.get("USERNAME"),
                "password" : os.environ.get("PASSWORD"),
                "database" : os.environ.get("DATABASE"),
                "collection" : os.environ.get("COLLECTION"),
                "port": int(os.environ.get("PORT"))}
    except:
        return None
            
def access_collection():
    """ Access the mongo 

    Returns:
        tuple: the first element is a boolean (True if there's no error) and the second element is a collection object.
    """
    parameters = load_parameters()
    client     = mongo_utils.connect_to_mongo(parameters["connection_url"], parameters["username"], parameters["password"], parameters["database"], parameters["port"])
    db         = mongo_utils.get_mongo_database(client, parameters["database"])   
    collection = mongo_utils.get_mongo_collection(db, parameters["collection"])

    return (collection is not None, collection)


if __name__ == "__main__":
    print(parse_pages())
    exit()
    no_error, collection = access_collection()

    if no_error:
        thesis = Thesis(4895, "Um teste para um teste", ["bruno", "pedro"], ["professor1", "professor2"], "https://teste.com.br", ["teste"], "UFRJ", "POLI", "Engenharia de Computação e Informação", "pt-br", 2021)
        mongo_utils.insert_document_on_mongo(collection, thesis.serialize())