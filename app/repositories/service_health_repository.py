"""
This module provides functionality to interact with the database to read the information
about the database being used.
"""

from typing import Any
from loguru import logger
from sqlalchemy import Engine, Row, text

from app.constants.sql_query_file_path_constant import GET_DATABASE_INFORMATION
from app.exceptions.custom_application_exceptions import DatabaseEngineNotInitializedException
from app.utilities.common_utility import get_sql_query_from_file
from app.utilities.database_utility import DatabaseUtility


def get_database_info() -> str | None:
    """
    Get the information of the database being used.

    Returns:
        str | None: The information of the database being used if available, otherwise None.

    Raises:
        DatabaseEngineNotInitializedException: If the database engine is not initialized.
    """

    # get instance of the database engine
    logger.info('retrieving database engine instance')
    __engine: Engine | None = DatabaseUtility.get_database_engine()

    # check if an instance of engine was received
    if __engine is not None:
        # fetch sql query from file
        logger.info(f'retrieving sql query from file path - {GET_DATABASE_INFORMATION}')
        __query_str: str = get_sql_query_from_file(
                    file_path=GET_DATABASE_INFORMATION)

        # open context manager
        logger.debug('trying to connect to the database')
        with __engine.connect() as connection:
            # execute sql query with corresponding parameters
            logger.debug('trying to execute retrieved sql query')
            __result: Row[Any] | None = connection.execute(
                statement=text(text=__query_str)).first()

            # return database information if available, else return None
            logger.info(f'retrieved database information successfully - {__result}')
            return __result[0] if __result is not None else None
    # else raise corresponding exception
    else:
        logger.error('no database engine instance available')
        raise DatabaseEngineNotInitializedException()
