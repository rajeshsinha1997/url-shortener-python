"""
Module: health_service_interface

This module defines the interface for health service classes in the application.
"""

from abc import ABC, abstractmethod

from app.interfaces.repositories.url_shortener_repository_interface import IUrlShortenerRepository
from app.models.response_model import HealthResponse


class IHealthService(ABC):
    """
    Interface for health service classes.

    This interface defines methods for retrieving health information.
    """

    def __init__(self, url_shortener_repository: IUrlShortenerRepository) -> None:
        """
        Initializes a new instance of the IUrlShortenerRepository interface.

        Parameters:
            url_shortener_repository (IUrlShortenerRepository): An instance of a class 
            implementing the IUrlShortenerRepository interface.

        Returns:
            None
        """

        # call super class constructor
        super().__init__()

        # create instance variable to hold reference to the repository instance
        self.__url_shortener_repository: IUrlShortenerRepository = url_shortener_repository

    @property
    def url_shortener_repository(self) -> IUrlShortenerRepository:
        """
        Getter property for the url shortener repository.

        Returns:
            IUrlShortenerRepository: An instance of a class implementing 
            the IUrlShortenerRepository interface.
        """

        # return instance of the repository
        return self.__url_shortener_repository

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
