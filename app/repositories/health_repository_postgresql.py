"""
Module: health_repository_postgresql

This module contains the implementation of the IHealthRepository interface for PostgreSQL databases.
"""

from typing import Any
from loguru import logger
from sqlalchemy import Engine, Row, text

from app.constants.application_constant import APPLICATION_STATUS_UP
from app.constants.sql_query_file_path_constant import GET_DATABASE_INFORMATION
from app.interfaces.repositories.health_repository_interface import IHealthRepository
from app.dto.database_information_dto import DatabaseInformationDTO
from app.utilities.common_utility import get_sql_query_from_file


class HealthRepositoryPostgreSQLImpl(IHealthRepository):
    """
    Implementation of the IHealthRepository interface for PostgreSQL databases.

    This class provides methods to interact with a PostgreSQL database and
    retrieve health-related information.
    """

    def __init__(self, engine: Engine) -> None:
        super().__init__(engine=engine)

    def get_database_information(self) -> DatabaseInformationDTO:
        # create variable to store database information
        __database_information: DatabaseInformationDTO = DatabaseInformationDTO()

        # retrieve sql query
        __sql_query: str = get_sql_query_from_file(
            file_path=GET_DATABASE_INFORMATION)

        # open context manager
        logger.debug('connecting to the database')
        with self.database_engine.connect() as connection:
            # execute sql query with corresponding parameters
            logger.debug('retrieving database information')
            __result: Row[Any] | None = connection.execute(
                statement=text(text=__sql_query)).first()

            # check if retrieved database information is not None
            if __result is not None:
                # split the database information by spaces
                __db_information_list: list[str] = __result.split()

                # update the database information
                __database_information.database_name = __db_information_list[0]
                __database_information.database_version = __db_information_list[1]
                __database_information.database_connectivity = APPLICATION_STATUS_UP

        # return database information
        logger.info(
            f'retrieved database information - {__database_information}')
        return __database_information
