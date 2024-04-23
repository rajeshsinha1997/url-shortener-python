from abc import ABC, abstractmethod
from sqlalchemy import Engine

from app.dto.database_information_dto import DatabaseInformationDTO
from app.models.database_model import UrlData


class IUrlShortenerRepository(ABC):
    """
    Interface for URL shortener repository classes.

    This interface defines the methods for interacting with the database 
    in a URL shortener application.
    """

    def __init__(self, engine: Engine) -> None:
        """
        Initialize a new instance of the class implementing IUrlShortenerRepository interface.

        Parameters:
            engine (Engine): The SQLAlchemy Engine object representing the database connection.

        """

        # call super class constructor
        super().__init__()

        # create instance variable to store reference to the database engine instance
        self.__database_engine: Engine = engine

    @property
    def database_engine(self) -> Engine:
        """
        Getter property for the database engine.

        Returns:
            Engine: The SQLAlchemy Engine object representing the database connection.
        """

        # return instance of the database engine
        return self.__database_engine

    @abstractmethod
    def get_database_information(self) -> DatabaseInformationDTO:
        """
        Method to retrieve information of the database.

        Returns:
            DatabaseInformationDTO: An instance of DatabaseInformationDTO class, containing
            all required information of the database being used.
        """

    @abstractmethod
    def find_short_url_value_by_long_url_hash(self, long_url_hash: str) -> str | None:
        """
        Method to find the short URL value associated with the given long URL hash.

        Parameters:
            long_url_hash (str): The hash of the long URL to search for.

        Returns:
            Union[str, None]: The short URL value if found, else None.
        """

    @abstractmethod
    def add_shortened_url_record(self, record_to_add: UrlData) -> None:
        """
        Method to add a new record into the database to store the generated 
        shortened URL value

        Parameters:
            record_to_add (UrlDatabaseRecord): An instance of UrlDatabaseRecord containing
            all required data to be added to the database.

        Returns:
            None
        """
