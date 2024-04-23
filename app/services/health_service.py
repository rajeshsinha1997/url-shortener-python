"""
Module: health_service

This module defines a service class HealthServiceImpl for providing the
health check related services.
"""

import os
from loguru import logger
from sqlalchemy.exc import DBAPIError
from app.constants.application_constant import \
    APPLICATION_NAME, APPLICATION_STATUS_DOWN, APPLICATION_STATUS_UP
from app.interfaces.repositories.health_repository_interface import IHealthRepository
from app.interfaces.services.health_service_interface import IHealthService
from app.models.response_model import HealthResponse
from app.dto.database_information_dto import DatabaseInformationDTO
from app.utilities.common_utility import get_current_time_stamp


class HealthServiceImpl(IHealthService):
    """
    Implementation of the IHealthService interface.

    This class provides methods to retrieve health-related information.
    """

    def __init__(self, health_repository: IHealthRepository) -> None:
        # call super class constructor
        super().__init__(health_repository=health_repository)

    def get_database_health(self) -> HealthResponse:
        # generate initial health information for the database service
        logger.info('generating health data for the database service')
        __database_health: HealthResponse = HealthResponse(
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
            __database_info: DatabaseInformationDTO = \
                self.health_repository.get_database_information()

            # update database health information
            __database_health.application_name = __database_info.database_name
            __database_health.application_version = __database_info.database_version
            __database_health.application_status = __database_info.database_connectivity
        except (DBAPIError) as e:
            # log error
            logger.error(f'unable to retrieve database information - {e}')

        # return database health
        return __database_health

    def get_health(self) -> HealthResponse:
        # generate application health data
        logger.info('generating application health data')
        __health_response = HealthResponse(
            params={
                'current_timestamp': get_current_time_stamp(),
                'application_name': APPLICATION_NAME,
                'application_version': os.environ.get('APPLICATION_VERSION') or 'N.A.',
                'application_status': APPLICATION_STATUS_UP
            })

        logger.info('adding service health data for the connected services')

        # add service-health data for the database service
        __health_response.connected_services_health.append(
            self.get_database_health()
        )
        logger.debug('added health data for the database service')

        # return service-health response
        logger.info(
            f'generated health data - {__health_response}')
        return __health_response
