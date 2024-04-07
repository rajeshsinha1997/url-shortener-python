"""
Module: url_shortener_repository

This module provides functions which allow us to interact with the database
related to url shortening functionality.
"""


from sqlalchemy import Engine, text
from app.models.db.database_model import UrlData
from app.utilities.common_utility import get_sql_query_from_file
from app.utilities.database_utility import DatabaseUtility
from app.constants.sql_query_file_path_constant import INSERT_SHORT_URL
from app.exceptions.custom_application_exceptions import \
    DatabaseEngineNotInitializedException


def add_shortened_url_record(record_to_add: UrlData) -> None:
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
        __query_str: str = get_sql_query_from_file(file_path=INSERT_SHORT_URL)

        # open context manager
        with __engine.begin() as connection:
            # execute sql query with corresponding parameters
            connection.execute(
                statement=text(text=__query_str),
                parameters={'short_url_value': record_to_add.short_url,
                            'long_url_value': record_to_add.long_url,
                            'created_at': record_to_add.created_on,
                            'last_used_on': record_to_add.last_used_on
                            }
                )
    # else raise corresponding exception
    else:
        raise DatabaseEngineNotInitializedException()
