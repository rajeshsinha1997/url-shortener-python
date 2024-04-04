"""
Module: url_shortener_repository

This module provides functions which allow us to interact with the database
related to url shortening functionality.
"""


import os
from typing import Any
from sqlalchemy import Engine, Row, text
from app.models.db.database_model import UrlDatabaseRecord
from app.utilities.database_utility import DatabaseUtility
from app.constants.sql_query_file_path_constant import \
    FIND_RECORD_BY_LONG_URL, INSERT_SHORT_URL, UPDATE_RECORD_DELETED_STATUS
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


def find_record_by_long_url(long_url: str) -> UrlDatabaseRecord | None:
    """
    Find a database record corresponding to the given long URL value.

    Parameters:
        long_url (str): The long URL to be used for searching of the existing short URL.

    Returns:
        UrlDatabaseRecord: An instance of UrlDatabaseRecord, containing all required
        data from the database record if found any, else None.

    Raises:
        DatabaseEngineNotInitializedException: If the database engine is not initialized.
    """

    # get instance of the database engine
    __engine: Engine | None = DatabaseUtility.get_database_engine()

    # check if an instance of engine was received
    if __engine is not None:
        # fetch sql query from file
        __query_str: str = __get_sql_query_from_file(
                    file_path=FIND_RECORD_BY_LONG_URL)

        # open context manager
        with __engine.begin() as connection:
            # execute sql query with corresponding parameters
            __result: Row[Any] | None = connection.execute(
                statement=text(text=__query_str),
                parameters={'l_url': long_url}).first()

            # check if a row is present in the result and contains the value for the
            # corresponding attribute
            if __result is not None:
                # return the result
                return UrlDatabaseRecord(
                    short_url=__result.s_url,
                    long_url=__result.l_url,
                    deleted=__result.deleted == 1,
                    created_on=__result.created_at
                )

            # else return None as result if no row was present or the result does not
            # contain the required attribute
            return None
    # else raise corresponding exception
    else:
        raise DatabaseEngineNotInitializedException()


def add_shortened_url_record(record_to_add: UrlDatabaseRecord) -> None:
    """
    Add a new record into the database to store the generated shortened URL value

    Parameters:
        record_to_add (UrlDatabaseRecord): An instance of UrlDatabaseRecord containing
        all required data to be added to the database.

    Returns:
        None

    Raises:
        DatabaseEngineNotInitializedException: If the database engine is not initialized.
    """

    # get instance of the database engine
    __engine: Engine | None = DatabaseUtility.get_database_engine()

    # check if an instance of engine was received
    if __engine is not None:
        # fetch sql query from file
        __query_str: str = __get_sql_query_from_file(file_path=INSERT_SHORT_URL)

        # open context manager
        with __engine.begin() as connection:
            # execute sql query with corresponding parameters
            connection.execute(
                statement=text(text=__query_str),
                parameters={'s_url': record_to_add.short_url,
                            'l_url': record_to_add.long_url,
                            'deleted': 1 if record_to_add.deleted else 0,
                            'created_at': record_to_add.created_on}
                )
    # else raise corresponding exception
    else:
        raise DatabaseEngineNotInitializedException()


def update_record_deleted_status(short_url: str, deleted: bool) -> None:
    """
    Update the 'deleted' status of an existing URL record in the database

    Parameters:
        short_url (str): short URL value to find the existing URL record
        deleted (bool): updated value of the 'deleted' status

    Returns:
        None
    """

    # get instance of the database engine
    __engine: Engine | None = DatabaseUtility.get_database_engine()

    # check if an instance of engine was received
    if __engine is not None:
        # fetch sql query from file
        __query_str: str = __get_sql_query_from_file(file_path=UPDATE_RECORD_DELETED_STATUS)

        # open context manager
        with __engine.begin() as connection:
            # execute sql query with corresponding parameters
            connection.execute(
                statement=text(text=__query_str),
                parameters={
                    'deleted': 1 if deleted else 0,
                    's_url': short_url
                    }
                )
    # else raise corresponding exception
    else:
        raise DatabaseEngineNotInitializedException()
