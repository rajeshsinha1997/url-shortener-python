"""
Module: service_health_service

This module is responsible for processing the business logics and building the service-health
responses for the URL shortener application.
"""

from sqlalchemy.exc import OperationalError
from app.constants.application_constant import \
    APPLICATION_NAME, APPLICATION_STATUS_DOWN, APPLICATION_STATUS_UP
from app.exceptions.custom_application_exceptions import DatabaseEngineNotInitializedException
from app.models.api.response_model import ServiceHealthResponse
from app.repositories.service_health_repository import get_database_info
from app.utilities.common_utility import get_current_time_stamp


def __get_database_service_health() -> ServiceHealthResponse:
    """
    Get the health check result of the database service being used.

    Returns:
        ServiceHealthResponse: A ServiceHealthResponse object containing the health check result.
            If the database information is not available or the database engine is not initialized,
            a default ServiceHealthResponse object with application status 'APPLICATION_STATUS_DOWN'
            a default application name and version will be returned.
    """

    # create database service health data object
    __connected_database_health: ServiceHealthResponse = ServiceHealthResponse(
        current_timestamp=get_current_time_stamp(),
        application_name='DATABASE',
        application_version='',
        application_status=APPLICATION_STATUS_DOWN,
        connected_services_health=[])

    # try to access the database
    try:
        # get information of the database being used
        __database_info: str | None = get_database_info()

        # check if database information was found
        if __database_info is not None:
            # split the database information by spaces and update the
            __database_information_list: list[str] = __database_info.split()

            # update the database name in the service health data object
            __connected_database_health.application_name = __database_information_list[0]

            # update the database version in the service health data object
            __connected_database_health.application_version = __database_information_list[1]

            # update connected database running status
            __connected_database_health.application_status = APPLICATION_STATUS_UP
    except (DatabaseEngineNotInitializedException, OperationalError):
        # add log statement
        pass

    # return database health
    return __connected_database_health


def build_service_health_response() -> ServiceHealthResponse:
    """
    Build a service-health response object.

    Returns:
        ServiceHealthResponse: An instance of ServiceHealthResponse representing the
        service-health response.
    """

    # build service health response object
    __service_health_response = ServiceHealthResponse(
        current_timestamp=get_current_time_stamp(),
        application_name=APPLICATION_NAME,
        application_version='0.0.1',
        application_status=APPLICATION_STATUS_UP,
        connected_services_health=[]
        )

    # add service-health data of connected database services
    __service_health_response.connected_services_health.append(
        __get_database_service_health()
    )

    # return service-health response
    return __service_health_response
