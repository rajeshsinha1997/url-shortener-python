"""
Module: service_factory

This module contains the ServiceFactory class, which is a factory for creating 
instances of service classes.
"""
from app.interfaces.repositories.health_repository_interface import IHealthRepository
from app.interfaces.services.health_service_interface import IHealthService
from app.services.health_service import HealthServiceImpl


class ServiceFactory:
    """
    Factory class for creating instances of service classes.
    """

    # class level variable to store the reference to the service class instance
    __health_service: IHealthService | None

    @classmethod
    def get_health_service(cls, health_repository: IHealthRepository) -> IHealthService:
        """
        Retrieve an instance of the health service.

        If an instance of the health service does not exist, create a new instance and return it.

        Parameters:
            health_repository (IHealthRepository): An instance of a class implementing the 
            IHealthRepository interface.

        Returns:
            IHealthService: An instance of a class implementing the IHealthService interface.
        """

        # check if an instance of the service does not exists
        if cls.__health_service is None:
            # create a new service instance
            cls.__health_service = HealthServiceImpl(
                health_repository=health_repository)

        # return the service instance
        return cls.__health_service
