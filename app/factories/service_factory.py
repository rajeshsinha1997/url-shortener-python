"""
Module: service_factory

This module contains the ServiceFactory class, which is a factory for creating 
instances of service classes.
"""
from app.interfaces.repositories.url_shortener_repository_interface import IUrlShortenerRepository
from app.interfaces.services.health_service_interface import IHealthService
from app.interfaces.services.url_shortener_service_interface import IUrlShortenerService
from app.services.health_service import HealthServiceImpl
from app.services.url_shortener_service import UrlShortenerServiceImpl


class ServiceFactory:
    """
    Factory class for creating instances of service classes.
    """

    # class level variable to store the reference of IHealthService
    __health_service: IHealthService | None = None

    # class level variable to store the reference of the IUrlShortenerService
    __url_shortener_service: IUrlShortenerService | None = None

    @classmethod
    def get_health_service(cls,
                           repository: IUrlShortenerRepository) -> IHealthService:
        """
        Retrieve an instance of a class implementing the IHealthService interface.

        If an instance of the class implementing the IHealthService interface
        does not exist, create a new instance and return it.

        Parameters:
            repository (IUrlShortenerRepository): An instance of a class implementing the 
            IUrlShortenerRepository interface.

        Returns:
            An instance of a class implementing IHealthService interface.
        """

        # check if an instance of the service does not exists
        if cls.__health_service is None:
            # create a new service instance
            cls.__health_service = HealthServiceImpl(
                url_shortener_repository=repository)

        # return the service instance
        return cls.__health_service

    @classmethod
    def get_url_shortener_service(cls,
                                  repository: IUrlShortenerRepository
                                  ) -> IUrlShortenerService:
        """
        Retrieve an instance of a class implementing the IUrlShortenerService interface.

        If an instance of the class implementing the IUrlShortenerService interface
        does not exist, create a new instance and return it.

        Parameters:
            repository (IUrlShortenerRepository): An instance of a class implementing the 
            IUrlShortenerRepository interface.

        Returns:
            An instance of a class implementing IUrlShortenerService interface.
        """

        # check if an instance of the service does not exists
        if cls.__url_shortener_service is None:
            # create a new service instance
            cls.__url_shortener_service = UrlShortenerServiceImpl(
                url_shortener_repository=repository
            )

        # return the service instance
        return cls.__url_shortener_service
