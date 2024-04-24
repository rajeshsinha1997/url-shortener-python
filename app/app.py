"""
Module: app

This module defines the UrlShortenerApplication class, which provides methods for creating, 
retrieving, and deleting a Flask application instance for the URL shortener service.
"""

from flask import Flask
from loguru import logger

from app.factories.repository_factory import RepositoryFactory
from app.factories.service_factory import ServiceFactory
from app.routes.url_shortener_route import UrlShortenerBlueprint
from app.routes.health_route import HealthBlueprint
from app.utilities.database_utility import DatabaseUtility


class UrlShortenerApplication:
    """
    A class for managing the Flask application instance for the URL shortener service.
    """

    # define class level private variables
    __application: Flask | None = None

    @classmethod
    def create_application(cls) -> None:
        """
        Create the Flask application instance if it has not been created already.

        This method checks if the Flask application instance has already been created. 
        If not, it creates a new Flask application using the current module name as the 
        import name. It then register the blueprints.

        Returns:
            None
        """

        # check if the application has not been created already
        logger.info(
            'checking if the url-shortener application has been initialized')
        if cls.__application is None:
            # create flask application
            logger.info('initializing the url-shortener application')
            cls.__application = Flask(import_name=__name__)

            # register health blueprint
            logger.info(
                'registering health blueprints to the url-shortener application')
            cls.__application.register_blueprint(blueprint=HealthBlueprint(
                name='health',
                import_name=__name__,
                url_prefix='/api/health',
                health_service=ServiceFactory.get_health_service(
                    repository=RepositoryFactory.get_health_repository(
                        database_engine=DatabaseUtility.get_database_engine()))))

            # register url-shortener blueprint
            cls.__application.register_blueprint(
                blueprint=UrlShortenerBlueprint(
                    name='url_shortener',
                    import_name=__name__,
                    url_prefix='/api/url',
                    url_shortener_service=ServiceFactory.get_url_shortener_service(
                        repository=RepositoryFactory.get_health_repository(
                            database_engine=DatabaseUtility.get_database_engine()))))
        logger.info('the url-shortener application has been initialized')

    @classmethod
    def get_application(cls) -> Flask | None:
        """
        Retrieve the Flask application instance.

        This method does not verify if an application instance has been created or not. It
        just returns the class level instance of the application.

        Returns:
            Flask or None: The Flask application instance if it has been created, otherwise None.
        """

        # return the application
        return cls.__application
