"""
Module: repository_factory

This module contains the RepositoryFactory class, which is a factory for creating 
instances of repository classes.
"""

from sqlalchemy import Engine
from app.interfaces.repositories.url_shortener_repository_interface \
    import IUrlShortenerRepository
from app.repositories.url_shortener_repository_postgresql import UrlShortenerRepositoryPostgreSQLImpl


class RepositoryFactory:
    """
    Factory class for creating instances of repository classes.
    """

    # class level variable to store reference to the repository class instance
    __health_repository: IUrlShortenerRepository | None = None

    @classmethod
    def get_health_repository(cls, database_engine: Engine) -> IUrlShortenerRepository:
        """
        Retrieve an instance of the health repository.

        If an instance of the health repository does not exist, create a new instance and return it.

        Parameters:
            database_engine (Engine): The SQLAlchemy Engine object representing the database 
            connection.

        Returns:
            IHealthRepository: An instance of a class implementing the 
            IUrlShortenerRepository interface.
        """

        # check if an instance of the repository does not exists
        if cls.__health_repository is None:
            # create a new repository instance
            cls.__health_repository = UrlShortenerRepositoryPostgreSQLImpl(
                engine=database_engine)

        # return the repository instance
        return cls.__health_repository
