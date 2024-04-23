"""
Module: health_service_interface

This module defines the interface for health service classes in the application.
"""

from abc import ABC, abstractmethod

from app.interfaces.repositories.health_repository_interface import IHealthRepository
from app.models.response_model import HealthResponse


class IHealthService(ABC):
    """
    Interface for health service classes.

    This interface defines methods for retrieving health information.
    """

    def __init__(self, health_repository: IHealthRepository) -> None:
        """
        Initializes a new instance of the IHealthService interface.

        Args:
            health_repository (IHealthRepository): An instance of a class implementing the 
            IHealthRepository interface.

        Returns:
            None
        """

        # call super class constructor
        super().__init__()

        # create instance variable to hold reference to the repository instance
        self.__health_repository: IHealthRepository = health_repository

    @property
    def health_repository(self) -> IHealthRepository:
        """
        Getter property for the health repository.

        Returns:
            IHealthRepository: An instance of a class implementing the IHealthRepository interface.
        """

        # return instance of the repository
        return self.__health_repository

    @abstractmethod
    def get_database_health(self) -> HealthResponse:
        """
        Method to retrieve the health status of the database.

        Returns:
            HealthResponse: An object representing the health status of the database.
        """

    @abstractmethod
    def get_health(self) -> HealthResponse:
        """
        Method to retrieve the overall health status of the service.

        Returns:
            HealthResponse: An object representing the overall health status of the service.
        """
