"""
Module: main

This module serves as the entry point for the URL shortener application. 
It initializes the database, the Flask application and retrieves the application instance
from the UrlShortenerApplication class.
"""

import os
from dotenv import load_dotenv
from flask import Flask
from loguru import logger
from app.app import UrlShortenerApplication
from app.utilities.database_utility import DatabaseUtility


# get current environment name
__environment: str | None = os.environ.get('APPLICATION_ENVIRONMENT')
logger.info(f'current environment - {__environment}')


# check if the current environment is not 'production'
if __environment != 'production':
    # load dotenv file
    logger.info('loading environment variables from dotenv file')
    load_dotenv()


# initialize database
logger.info('initializing database utility')
DatabaseUtility.initialize_database()


# create flask application
logger.info('creating url-shortener application')
UrlShortenerApplication.create_application()


# call method to get application
logger.info('retrieving url-shortener application instance')
app: Flask | None = UrlShortenerApplication.get_application()
