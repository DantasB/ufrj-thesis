import os
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