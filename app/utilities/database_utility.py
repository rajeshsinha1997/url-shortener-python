"""
Module: database_utility

This module provides a utility class for managing database connections and operations.
"""

import os
from sqlalchemy import Engine, create_engine

from app.exceptions.application_initialization_exception import ApplicationInitializationException


class DatabaseUtility:
    """
    Utility class for managing database connections and operations.
    """

    # create variable to hold database engine instance
    __engine: Engine | None = None

    @classmethod
    def initialize_database(cls) -> None:
        """
        Initialize the database engine.

        This method initializes the database engine if it has not been initialized already.
        It retrieves the database URL from the environment variables and creates a database engine
        using SQLAlchemy's `create_engine` function.

        Raises:
            ApplicationInitializationException: If the database URL is not found in the
            environment variables.

        Returns:
            None
        """

        # check if the engine is not yer initialized
        if cls.__engine is None:
            # get database url from environment variable
            __database_url: str | None = os.environ.get('DATABASE_URL')

            # check if a value of database url was not found in the environment variables
            if __database_url is None:
                # raise corresponding exception
                raise ApplicationInitializationException(
                    exception_message=f'INVALID DATABASE URL: {__database_url}')

            # create database engine
            cls.__engine = create_engine(url=__database_url, echo=True)
