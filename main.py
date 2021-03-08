from Classes.thesis_object import Thesis
from crawler.thesis_crawler import get_thesis_objects
from SharedLibrary.mongo_utils import access_collection, get_mongo_monographs_id
from SharedLibrary.mongo_utils import insert_document_on_mongo
from SharedLibrary.env_utils import load_parameters       

if __name__ == "__main__":
    no_error, collection = access_collection(load_parameters())
    if not no_error:
        exit()
    
    THESIS_IDS = get_mongo_monographs_id(collection)
    thesis_list = get_thesis_objects(THESIS_IDS)
    if no_error:
        for thesis in thesis_list:
            insert_document_on_mongo(collection, thesis.serialize())