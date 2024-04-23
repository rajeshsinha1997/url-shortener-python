"""
Module: health_repository_interface

This module defines the interface for health repository classes in the application.
"""

from abc import ABC, abstractmethod
from sqlalchemy import Engine

from app.dto.database_information_dto import DatabaseInformationDTO


class IHealthRepository(ABC):
    """
    Interface for health repository classes.

    This interface defines methods for retrieving database information.
    """

    def __init__(self, engine: Engine) -> None:
        """
        Initializes a new instance of the class implementing IHealthRepository interface.

        Args:
            engine (Engine): The SQLAlchemy Engine object representing the database connection.

        Returns:
            None
        """

        # call super class constructor
        super().__init__()

        # create instance variable to hold reference to the database engine instance
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
