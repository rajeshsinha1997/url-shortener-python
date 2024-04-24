"""
Module: url_shortener_service_interface

This module defines the interface for URL shortener services.
"""

from abc import ABC, abstractmethod

from app.interfaces.repositories.url_shortener_repository_interface import IUrlShortenerRepository


class IUrlShortenerService(ABC):
    """
    Interface for URL shortener service.

    This interface defines the contract for URL shortener services.
    """

    def __init__(self, url_shortener_repository: IUrlShortenerRepository) -> None:
        """
        Initializes the URL shortener service with the specified URL shortener repository.

        Parameters:
            url_shortener_repository (IUrlShortenerRepository): The URL shortener repository 
            to be associated with the service.

        Returns:
            None
        """

        # call super class constructor
        super().__init__()

        # create instance variable to hold the reference to the repository instance
        self.__url_shortener_repository: IUrlShortenerRepository = url_shortener_repository

    @property
    def url_shortener_repository(self) -> IUrlShortenerRepository:
        """
        Getter method to retrieve the URL shortener repository associated with the service.

        Returns:
            IUrlShortenerRepository: The URL shortener repository.
        """

        # return the instance of the repository
        return self.__url_shortener_repository

    @abstractmethod
    def create_short_url_from_long_url(self, long_url: str) -> str:
        """
        Create a shortened URL from the provided long URL value

        Parameters:
            long_url (str): the long URL required to be shortened

        Returns:
            str: shortened version of the provided long URL as string
        """
