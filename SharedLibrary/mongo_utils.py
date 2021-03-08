import pymongo

def connect_to_mongo(base_uri, user, password, database, port):
    """ Connect to mongo using the Atlas uri

    Args:
        base_uri (str): uri to be filled with the user informations
        user (str): user login
        password (str): user password
        database (str): database to connect
        port (int): mongo cluster port

    Returns:
        MongoClient: the client to be used in the database/collection access
    """
    try:
        connection_string = base_uri.format(user=user, password=password, database=database)
        return pymongo.MongoClient(connection_string, port)
    except:
        return None

def get_mongo_database(connection, database_name):
    """ Access the database

    Args:
        connection (MongoClient): Mongo connection to the database
        database_name (str): database to be accessed

    Returns:
        Database: the Database object
    """
    try:
        return connection.get_database(database_name)
    except:
        return None

def get_mongo_collection(database, collection_name):
    """ Access the collection

    Args:
        database (Database): Database that contains the collection_name
        collection_name (str): collection to be accessed

    Returns:
        Collection: the Collection object
    """
    try:
        return database.get_collection(collection_name)
    except:
        return None

def insert_document_on_mongo(collection, document):
    """ Inserts a single document to the collection

    Args:
        collection (Collection): collection object to insert the document
        document (Response): Response object to be saved on mongo

    Returns:
        bool: True if document was inserted
    """
    print("[Debug] Inserting document on mongo")
    try:
        collection.insert_one(document)
        print("[Debug] Document inserted on mongo")
        return True       
    except:
        print("[Warn] Couldn't insert the document")
        raise
        return False

def delete_document_on_mongo(collection, query):
    """ Deletes a single document to the collection

    Args:
        collection (Collection): collection object to insert the document
        query (dictionary): Query used to find the object and delete it in the collection

    Returns:
        bool: True if document was deleted correctly
    """
    print("[Debug] Deleting document on mongo")
    try:
        collection.delete_one(query)
        print("[Debug] Document deleted")
        return True       
    except:
        print("[Warn] Couldn't delete the document")
        return False

def get_mongo_monographs_id(collection):
    """ Gets a list of existing ThesisId on Mongo

    Args:
        collection (Collection): collection object to get the ThesisId

    Returns:
        list: the list of ThesisId
    """
    try:
        return list(collection.distinct("ThesisId"))
    except:
        return None

def access_collection(parameters):
    """ Access the mongo 
    Args:
        parameters (dictionary): dictionary object to with the env parameters
    Returns:
        tuple: the first element is a boolean (True if there's no error) and the second element is a collection object.
    """
    if (parameters is None):
        return (False, None)

    client     = connect_to_mongo(parameters["connection_url"], parameters["username"], parameters["password"], parameters["database"], parameters["port"])
    db         = get_mongo_database(client, parameters["database"])   
    collection = get_mongo_collection(db, parameters["collection"])

    return (collection is not None, collection)