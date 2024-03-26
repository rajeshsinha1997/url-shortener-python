"""
Module: service_health_service

This module is responsible for processing the business logics and building the service-health
responses for the URL shortener application.
"""

from app.constants.application_constant import APPLICATION_NAME
from app.constants.application_constant import APPLICATION_STATUS_UP
from app.models.api.response_model import ServiceHealthResponse
from app.utilities.common_utility import get_current_time_stamp


def build_service_health_response() -> ServiceHealthResponse:
    """
    Build a service-health response object.

    Returns:
        ServiceHealthResponse: An instance of ServiceHealthResponse representing the
        service-health response.
    """

    # build service health response object
    service_health_response = ServiceHealthResponse(
        current_timestamp=get_current_time_stamp(),
        application_name=APPLICATION_NAME,
        application_status=APPLICATION_STATUS_UP,
        connected_services_health=[]
        )

    # add service-health data of connected services

    # return service-health response
    return service_health_response
