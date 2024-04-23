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

    Attributes:
        health_repository (IHealthRepository): An instance of a class implementing the 
        IHealthRepository interface, providing access to health-related data.

    Methods:
        get_database_health: An abstract method to retrieve the health status of the database.
        get_health: An abstract method to retrieve the overall health status of the service.

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
        super().__init__()
        self.__health_repository: IHealthRepository = health_repository

    @property
    def health_repository(self) -> IHealthRepository:
        """
        Getter property for the health repository.

        Returns:
            IHealthRepository: An instance of a class implementing the IHealthRepository interface.
        """
        return self.__health_repository

    @abstractmethod
    def get_database_health(self) -> HealthResponse:
        """
        Abstract method to retrieve the health status of the database.

        Returns:
            HealthResponse: An object representing the health status of the database.
        """

    @abstractmethod
    def get_health(self) -> HealthResponse:
        """
        Abstract method to retrieve the overall health status of the service.

        Returns:
            HealthResponse: An object representing the overall health status of the service.
        """
