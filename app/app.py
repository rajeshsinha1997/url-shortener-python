"""
Module: app

This module defines the UrlShortenerApplication class, which provides methods for creating, 
retrieving, and deleting a Flask application instance for the URL shortener service.
"""

from flask import Flask
from loguru import logger

from app.routes.url_shortener_route import url_shortener_blueprint
from app.routes.service_health_route import service_health_blueprint


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
            logger.debug('initializing the url-shortener application')
            cls.__application = Flask(import_name=__name__)

            # register blueprints
            logger.info(
                'registering blueprints to the url-shortener application')
            cls.__application.register_blueprint(
                blueprint=service_health_blueprint)
            cls.__application.register_blueprint(
                blueprint=url_shortener_blueprint)
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
