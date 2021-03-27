class Thesis():
    """ Used to define all the characteristics of a thesis.

    Args:
        thesis_id (int): thesis identifier
        title (str): thesis title
        authors (list): list of the authors who writed the thesis
        advisors (list): list of advisors who helped this theses
        url (str): url to the thesis pdf
        keywords (list): keywords that relates to the thesis theme.
        university (str): university name
        institution (str): institution name
        course (str): authors course name 
        language (str): language that the thesis got published.
        year (int): year that the thesis got published
    """

    def __init__(self, thesis_id, title, authors, advisors, url, keywords, university, institution, course, language, year):
        self.thesis_id = thesis_id
        self.title = title
        self.url = url
        self.authors = authors
        self.advisors = advisors
        self.keywords = keywords
        self.university = university
        self.institution = institution
        self.course = course
        self.language = language
        self.year = year

    def __eq__(self, thesis):
        if self.title == thesis.title:
            return True
        return False

    def serialize(self):
        """Serializes the Thesis Object

        Returns:
            dictionary: serialized object
        """
        return {"ThesisId": self.thesis_id,
                "Title": self.title,
                "Url": self.url,
                "Authors": self.authors,
                "Advisors": self.advisors,
                "Keywords": self.keywords,
                "University": self.university,
                "Institution": self.institution,
                "Course": self.course,
                "Language": self.language,
                "Year": self.year}
