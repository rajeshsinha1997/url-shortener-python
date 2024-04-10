"""
Module: service_health_service

This module is responsible for processing the business logics and building the service-health
responses for the URL shortener application and the connected external services.
"""

import os
from loguru import logger
from sqlalchemy.exc import DBAPIError
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

    logger.info('generating service health data for database')

    # create database service health data object
    __connected_database_health: ServiceHealthResponse = ServiceHealthResponse(
        params={
            'current_timestamp': get_current_time_stamp(),
            'application_name': 'DATABASE',
            'application_version': '',
            'application_status': APPLICATION_STATUS_DOWN
        })

    # try to access the database
    try:
        # get information of the database being used
        logger.debug('trying to retrieve database information')
        __database_info: str | None = get_database_info()

        # check if database information was found
        if __database_info is not None:
            logger.debug('retrieved database information successfully')

            # split the database information by spaces
            __database_information_list: list[str] = __database_info.split()

            # update the database name in the service health data object
            __connected_database_health.application_name = __database_information_list[0]

            # update the database version in the service health data object
            __connected_database_health.application_version = __database_information_list[1]

            # update connected database running status
            __connected_database_health.application_status = APPLICATION_STATUS_UP
        else:
            # log warning message
            logger.warning('no database information was found')
    except (DatabaseEngineNotInitializedException, DBAPIError) as e:
        # log error
        logger.error(f'unable to retrieve database information - {e}')

    # return database health
    logger.info(f'generated service health data for database - {__connected_database_health}')
    return __connected_database_health


def build_service_health_response() -> ServiceHealthResponse:
    """
    Build a service-health response object.

    Returns:
        ServiceHealthResponse: An instance of ServiceHealthResponse representing the
        service-health response.
    """

    logger.info('generating service health data')

    # build service health response object
    __service_health_response = ServiceHealthResponse(
        params={
            'current_timestamp': get_current_time_stamp(),
            'application_name': APPLICATION_NAME,
            'application_version': os.environ.get('APPLICATION_VERSION') or 'N.A.',
            'application_status': APPLICATION_STATUS_UP
        })

    logger.debug('adding service health data for connected services')

    # add service-health data of connected database services
    __service_health_response.connected_services_health.append(
        __get_database_service_health()
    )

    # return service-health response
    logger.info(f'generated service health data - {__service_health_response}')
    return __service_health_response
