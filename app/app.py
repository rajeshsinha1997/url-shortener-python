"""
Module: app

This module defines the UrlShortenerApplication class, which provides methods for creating, 
retrieving, and deleting a Flask application instance for the URL shortener service.
"""

from flask import Flask

from app.routes.service_health_route import service_health_blueprint


class UrlShortenerApplication:
    """
    A class for managing the Flask application instance for the URL shortener service.
    """

    # define class level private variables
    __application: Flask | None = None

    @classmethod
    def __create_application(cls) -> None:
        """
        Create the Flask application instance if it has not been created already.

        This method checks if the Flask application instance has already been created. 
        If not, it creates a new Flask application using the current module name as the 
        import name. It then register the blueprints.

        Returns:
            None
        """

        # check if the application has not been created already
        if cls.__application is None:
            # create flask application
            cls.__application = Flask(import_name=__name__)

            # register blueprints
            cls.__application.register_blueprint(blueprint=service_health_blueprint)

    @classmethod
    def get_application(cls) -> Flask | None:
        """
        Retrieve the Flask application instance.

        Returns:
            Flask or None: The Flask application instance if it has been created, otherwise None.

        Notes:
            If the application has not been created yet, this method will call the private
            `__create_application` method to create the application instance.
        """

        # check if the application has not been created
        if cls.__application is None:
            # call method to create application
            cls.__create_application()

        # return the application
        return cls.__application
