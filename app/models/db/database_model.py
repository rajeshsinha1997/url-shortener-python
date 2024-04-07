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

    def __init__(self, params: dict[str, str]) -> None:
        """
        Initialize a new URL record instance.

        Parameters:
            params (dict): A dictionary containing the following key-value pairs:
                - 'short_url' (str): The shortened URL.
                - 'long_url' (str): The original long URL.
                - 'long_url_hash' (str): Hash value for the original long URL.
                - 'created_on' (str): The timestamp when the record was created.
                - 'last_used_on' (str): The timestamp when this shortened URL was
                                        last used.
        """

        self.short_url: str = params['short_url']
        self.long_url: str = params['long_url']
        self.long_url_hash: str = params['long_url_hash']
        self.created_on: str = params['created_on']
        self.last_used_on: str = params['last_used_on']

    def __str__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """

        return (
            f'Short URL: {self.short_url}'
            f'Long URL: {self.long_url}'
            f'Long URL Hash: {self.long_url_hash}'
            f'Created On: {self.created_on}'
            f'Last Used On: {self.last_used_on}'
        )

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """

        return self.__str__()
