"""
Module: health_repository_interface

This module defines the interface for health repository classes in the application.
"""

from abc import ABC, abstractmethod
from sqlalchemy import Engine

from app.models.dto.database_information_dto import DatabaseInformationDTO


class IHealthRepository(ABC):
    """
    Interface for health repository classes.

    This interface defines methods for retrieving database information.

    Attributes:
        database_engine (Engine): The SQLAlchemy Engine object representing the database connection.

    Methods:
        get_database_information: An abstract method to retrieve information of the database.

    """

    def __init__(self, engine: Engine) -> None:
        """
        Initializes a new instance of the IHealthRepository interface.

        Args:
            engine (Engine): The SQLAlchemy Engine object representing the database connection.

        Returns:
            None
        """
        super().__init__()
        self.__database_engine: Engine = engine

    @property
    def database_engine(self) -> Engine:
        """
        Getter property for the database engine.

        Returns:
            Engine: The SQLAlchemy Engine object representing the database connection.
        """
        return self.__database_engine

    @abstractmethod
    def get_database_information(self) -> DatabaseInformationDTO:
        """
        Abstract method to retrieve information of the database.

        Returns:
            DatabaseInformationDTO: An instance of DatabaseInformationDTO class, containing
            all required information of the database being used.
        """
