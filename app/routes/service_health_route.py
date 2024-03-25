"""
Module: service_health_route

This module defines a Flask Blueprint for handling health check endpoints of the 
URL shortener application.
"""

from flask import Blueprint, Response

from app.services.service_health_service import ServiceHealthService
from app.utilities.common_utility import build_response

# create blueprint
service_health_blueprint = Blueprint(name='health',
                                     import_name=__name__,
                                     url_prefix='/health/')


@service_health_blueprint.get(rule='/')
def get_service_health() -> Response:
    """
    Handler for the GET /health/ endpoint.

    Returns:
        Response: HTTP response containing the service health data.

    """

    # return service health response
    return build_response(
        response_data=ServiceHealthService.build_service_health_response(),
        response_status_code=200)
