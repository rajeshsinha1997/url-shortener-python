"""
Module: database_model

This module defines the classes, representing the structure of the corresponding
database tables.
"""


class UrlData:
    """
    An instance of this class represents a single database record from
    the table 'url_data'.

    This class represents a single database record from the 'url_data' table,
    storing information such as the short URL, long URL, deletion status,
    and creation timestamp.
    """

    def __init__(self, short_url: str, long_url: str, created_on: str, last_used_on: str) -> None:
        """
        Initialize a new URL record instance.

        Parameters:
            short_url (str): The shortened URL.
            long_url (str): The original long URL.
            created_on (str): The timestamp when the record was created.
            last_used_on (str): The timestamp when this shortened URL was last used
        """

        self.short_url: str = short_url
        self.long_url: str = long_url
        self.created_on: str = created_on
        self.last_used_on: str = last_used_on
