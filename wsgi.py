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
    ALLOWED_LOG_LEVELS, DEFAULT_LOG_LEVEL, LOG_OUTPUT_FILE_PATH, LOG_OUTPUT_FILE_ROTATION_SIZE
from app.utilities.database_utility import DatabaseUtility


# get current environment name
__environment: str | None = os.environ.get('APPLICATION_ENVIRONMENT')
logger.info(f'current environment - {__environment}')


# check if the current environment is not 'production'
if __environment is None or __environment.lower() != 'production':
    # load dotenv file
    logger.info('loading the environment variables from dotenv file')
    load_dotenv()


# retrieve required log level information from environment
__log_level: str | None = os.environ.get('LOG_LEVEL')


# remove existing log handlers
logger.remove()


# check if retrieved log level value is not valid
if __log_level is None or __log_level.upper() not in ALLOWED_LOG_LEVELS:
    # add new console log handler with default log level value
    logger.add(sink=sys.stdout,
               colorize=True,
               level=DEFAULT_LOG_LEVEL)

    # add new file log handler with default log level value
    logger.add(sink=LOG_OUTPUT_FILE_PATH,
               rotation=LOG_OUTPUT_FILE_ROTATION_SIZE,
               level=DEFAULT_LOG_LEVEL)
else:
    # add new console log handler with retrieved log level value
    logger.add(sink=sys.stdout,
               colorize=True,
               level=__log_level)

    # add new file log handler with default log level value
    logger.add(sink=LOG_OUTPUT_FILE_PATH,
               rotation=LOG_OUTPUT_FILE_ROTATION_SIZE,
               level=__log_level)


# initialize database
logger.info('initializing database utility')
DatabaseUtility.initialize_database()


# create flask application
logger.info('creating the url-shortener application')
UrlShortenerApplication.create_application()


# call method to get application
logger.info('retrieving the url-shortener application instance')
app: Flask | None = UrlShortenerApplication.get_application()
