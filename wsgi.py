"""
Module: main

This module serves as the entry point for the URL shortener application. 
It initializes the database, the Flask application and retrieves the application instance
from the UrlShortenerApplication class.
"""

import os
import sys
from dotenv import load_dotenv
from flask import Flask
from loguru import logger
from app.app import UrlShortenerApplication
from app.constants.application_constant import \
    DEFAULT_LOG_LEVEL, LOG_OUTPUT_FILE_PATH, LOG_OUTPUT_FILE_ROTATION_SIZE
from app.utilities.database_utility import DatabaseUtility
from app.utilities.validation_utility import is_valid_log_level


# get current environment name
__environment: str | None = os.environ.get('APPLICATION_ENVIRONMENT')
logger.info(f'initiating application on environment - {__environment}')


# check if the current environment is not 'production'
if __environment is None or __environment.lower() != 'production':
    # load dotenv file
    logger.info('loading the environment variables from dotenv file')
    load_dotenv()


# remove existing log handlers
logger.remove()


# retrieve required log level information from environment and validate
__log_level: str | None = os.environ.get('LOG_LEVEL')


# add new console log handler
logger.add(sink=sys.stdout,
            colorize=True,
            level= str(object=__log_level) if is_valid_log_level(
                log_level=__log_level) else DEFAULT_LOG_LEVEL)


# add new file log handler
logger.add(sink=LOG_OUTPUT_FILE_PATH,
            rotation=LOG_OUTPUT_FILE_ROTATION_SIZE,
            level=str(object=__log_level) if is_valid_log_level(
                log_level=__log_level) else DEFAULT_LOG_LEVEL)


# initialize database
logger.info('initializing database utility')
DatabaseUtility.initialize_database()


# create flask application
logger.info('creating the url-shortener application')
UrlShortenerApplication.create_application()


# call method to get application
logger.info('retrieving the url-shortener application instance')
app: Flask | None = UrlShortenerApplication.get_application()
