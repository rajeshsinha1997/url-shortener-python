"""
Module: database_utility

This module provides a utility class for managing database connections and operations.
"""


import os
from abc import ABC
from loguru import logger
from sqlalchemy import Engine, create_engine

from app.exceptions.custom_application_exceptions import ApplicationInitializationException


class DatabaseUtility(ABC):
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

        # check if the database engine is not yet initialized
        logger.info('checking if the database engine has been initialized')
        if cls.__engine is None:
            # retrieve the database url from the environment
            logger.debug('retrieving database URL from the environment')
            __database_url: str | None = os.environ.get('DATABASE_URL')

            # check if a value of database url was not found in the environment
            if __database_url is None:
                logger.error('no database URL found in the environment')

                # raise corresponding exception
                raise ApplicationInitializationException(
                    exception_message='NO DATABASE URL FOUND IN THE ENVIRONMENT')

            # retrieve 'echo' flag value from the environment
            logger.debug('retrieving \'echo\' flag value from the environment')
            __echo: str = os.environ.get('DATABASE_ECHO') or 'False'

            # create database engine
            logger.info(f'initializing the database engine with echo - {__echo}')
            cls.__engine = create_engine(url=__database_url, echo=__echo)
        logger.info('the database engine has been initialized')

    @classmethod
    def get_database_engine(cls) -> Engine | None:
        """
        Get an instance of the database engine.
        
        This method just returns the instance of the database engine available in this class,
        but does not verify whether an engine instance has been created or not.
        
        Returns:
            Instance of the database engine if already created, None otherwise.
        """

        # return instance of the database engine
        logger.debug('returning the database engine')
        return cls.__engine
