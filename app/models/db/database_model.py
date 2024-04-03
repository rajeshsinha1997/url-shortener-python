"""
Module: database_model

This module defines the classes, representing the structure of the corresponding
database tables.
"""


class UrlDatabaseRecord:
    """
    An instance of this class represents a single database record from
    the table 'urls'.

    This class represents a single database record from the 'urls' table,
    storing information such as the short URL, long URL, deletion status,
    and creation timestamp.
    """

    def __init__(self, short_url: str, long_url: str, deleted: bool, created_on: str) -> None:
        """
        Initialize a new URL record instance.

        Parameters:
            short_url (str): The shortened URL.
            long_url (str): The original long URL.
            deleted (bool): Indicates if the record is deleted or not.
            created_on (str): The timestamp when the record was created.
        """

        self.short_url: str = short_url
        self.long_url: str = long_url
        self.deleted: bool = deleted
        self.created_on: str = created_on
