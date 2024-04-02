"""
Module: url_shortener_repository

This module provides functions which allow us to interact with the database.
"""


import os
from typing import Any
from sqlalchemy import Engine, Row, text
from app.utilities.database_utility import DatabaseUtility
from app.constants.sql_query_file_path_constant import \
    FIND_SHORTENED_URL_BY_LONG_URL
from app.exceptions.custom_application_exceptions import \
    DatabaseEngineNotInitializedException, QueryFileNotFoundException


def __get_sql_query_from_file(file_path: str) -> str:
    """
    Get SQL query from a file.

    Parameters:
        file_path (str): The path to the file containing SQL query.

    Returns:
        str: The SQL query retrieved from the file.

    Raises:
        QueryFileNotFoundException: If the provided file path does not exist.
    """

    # check if the provided file path exists
    if os.path.exists(path=file_path):
        # open file present at the provided path in reading mode
        with open(file=file_path, mode='r', encoding='UTF-8') as query:
            # return the contents of the file into a variable
            return query.read()
    # else throw corresponding error
    else:
        raise QueryFileNotFoundException(
            exception_message=f'INVALID SQL QUERY FILE PATH: {file_path}')


def find_shortened_url_by_long_url(long_url: str) -> str | None:
    """
    Find the shortened version of a given long URL.

    Parameters:
        long_url (str): The long URL to search for.

    Returns:
        str: The shortened URL corresponding to the provided long URL.

    Raises:
        DatabaseEngineNotInitializedException: If the database engine is not initialized.
    """

    # get instance of the database engine
    __engine: Engine | None = DatabaseUtility.get_database_engine()

    # check if an instance of engine was received
    if __engine is not None:
        # fetch sql query from file
        __query_str: str = __get_sql_query_from_file(
                    file_path=FIND_SHORTENED_URL_BY_LONG_URL)

        # open context manager
        with __engine.begin() as connection:
            # execute sql query with corresponding parameters
            __result: Row[Any] | None = connection.execute(
                statement=text(text=__query_str),
                parameters={'l_url': long_url, 'deleted': 0}
                ).first()

            # check if a row is present in the result and contains the value for the
            # corresponding attribute
            if __result is not None and hasattr(__result, 's_url'):
                # return the shortened url from the result
                return __result.s_url

            # else return None as result if no row was present or the result does not
            # contain the required attribute
            return None
    # else raise corresponding exception
    else:
        raise DatabaseEngineNotInitializedException()
