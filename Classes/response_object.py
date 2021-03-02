from Classes.thesis_object import Thesis

class Response():
    """ Used to define the api response

    Args:
        thesis (Thesis, optional): the captured thesis. Defaults to None.
        error_message (str, optional): capture error message if there's any error. Defaults to "".
        success (bool, optional): true if there's no error during the capture. Defaults to False.
    """
    def __init__(self, thesis: Thesis = None, error_message = "", success = False):
        self.thesis        = thesis
        self.error_message = error_message
        self.success       = success
    
    def serialize(self):
        """Serializes the Response Object

        Returns:
            dictionary: serialized object
        """
        return {"Thesis" : self.thesis,
                "ErrorMessage" : self.error_message,
                "Success" : self.success }