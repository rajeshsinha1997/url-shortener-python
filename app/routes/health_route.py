"""
Module: health_route

This module defines a custom Blueprint subclass for handling health-related endpoints.
"""
from flask import Blueprint, Response, request
from loguru import logger

from app.interfaces.services.health_service_interface import IHealthService
from app.utilities.common_utility import build_response


class HealthBlueprint(Blueprint):
    """
    A custom Blueprint subclass for handling health-related endpoints.

    Note:
        This class extends the Flask Blueprint class, providing additional functionality
        specific to handling health-related endpoints.

    """

    def __init__(self,
                 name: str,
                 import_name: str,
                 url_prefix: str,
                 health_service: IHealthService) -> None:
        """
        Initializes a new instance of the HealthBlueprint class.

        Args:
            name (str): The name of the Blueprint.
            import_name (str): The import name of the Blueprint.
            url_prefix (str): The URL prefix for the Blueprint's routes.
            health_service (IHealthService): An instance of a class implementing the
                IHealthService interface, providing health-related functionality.

        Returns:
            None
        """

        logger.debug('initializing blueprint: HealthBlueprint')

        # call super class constructor
        super().__init__(name=name, import_name=import_name, url_prefix=url_prefix)

        # add service reference
        self.health_service: IHealthService = health_service

        # add url rule
        self.add_url_rule(rule='/', view_func=self.get_health)

        logger.info('initialized blueprint: HealthBlueprint')

    def get_health(self) -> Response:
        """
        Handler for the GET /api/health/ endpoint.

        Returns:
            Response: HTTP response containing the health data.
        """
        try:
            # log request
            logger.info(f'received {request.method} request to {request.url}')

            # return service health response
            logger.info('building health check response')
            return build_response(
                response_data=self.health_service.get_health(),
                response_status_code=200)
        except FileNotFoundError:
            # return 500 INTERNAL SERVER ERROR
            return build_response(response_data='some internal error occurred',
                                  response_status_code=500)
