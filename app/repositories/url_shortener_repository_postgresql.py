"""
Module: health_repository_postgresql

This module contains the implementation of the IHealthRepository interface for PostgreSQL databases.
"""

from typing import Any
from loguru import logger
from sqlalchemy import Engine, Row, text

from app.constants.application_constant import APPLICATION_STATUS_UP
from app.constants.sql_query_file_path_constant import \
    GET_DATABASE_INFORMATION, GET_SHORT_URL_BY_LONG_URL_HASH, INSERT_SHORT_URL
from app.dto.database_information_dto import DatabaseInformationDTO
from app.interfaces.repositories.url_shortener_repository_interface import IUrlShortenerRepository
from app.models.database_model import UrlData
from app.utilities.common_utility import get_sql_query_from_file


class UrlShortenerRepositoryPostgreSQLImpl(IUrlShortenerRepository):
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

    def find_short_url_value_by_long_url_hash(self, long_url_hash: str) -> str | None:
        # retrieve sql query from file
        logger.debug(
            f'retrieving the sql query from file path - {GET_SHORT_URL_BY_LONG_URL_HASH}')
        __query_str: str = get_sql_query_from_file(
            file_path=GET_SHORT_URL_BY_LONG_URL_HASH)

        # open context manager
        logger.debug('connecting to the database')
        with self.database_engine.begin() as connection:
            # execute sql query with corresponding parameters
            logger.debug(
                f'retrieving existing short URL using the long URL hash - {long_url_hash}')
            __result: Row[Any] | None = connection.execute(
                statement=text(text=__query_str),
                parameters={'long_url_hash': long_url_hash}
            ).first()

            # return short url value if any row was found, else return None
            logger.info(f'retrieved short URL \'{__result}\' using the long URL hash ' +
                        f'\'{long_url_hash}\'')
            return __result[0] if __result is not None else None

    def add_shortened_url_record(self, record_to_add: UrlData) -> None:
        # fetch sql query from file
        logger.debug(
            f'retrieving the sql query from file path - {INSERT_SHORT_URL}')
        __query_str: str = get_sql_query_from_file(
            file_path=INSERT_SHORT_URL)

        # open context manager
        logger.debug('connecting to the database')
        with self.database_engine.begin() as connection:
            # execute sql query with corresponding parameters
            logger.debug(
                f'adding a new short URL record to the database - {record_to_add}')
            connection.execute(
                statement=text(text=__query_str),
                parameters={'short_url_value': record_to_add.short_url,
                            'long_url_value': record_to_add.long_url,
                            'long_url_hash': record_to_add.long_url_hash,
                            'created_at': record_to_add.created_on,
                            'last_used_on': record_to_add.last_used_on
                            }
            )
            logger.info(
                f'added new short URL record to the database - {record_to_add}')
