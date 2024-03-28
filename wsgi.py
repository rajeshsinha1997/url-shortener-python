"""
Module: main

This module serves as the entry point for the URL shortener application. It initializes the database, the Flask application and retrieves the application instance from the UrlShortenerApplication class.
"""

import os
from dotenv import load_dotenv
from flask import Flask
from app.app import UrlShortenerApplication
from app.utilities.database_utility import DatabaseUtility

# check if the current environment is not 'production'
if os.getenv(key='environment') != 'production':
    # load dotenv file
    load_dotenv()

# initialize database
DatabaseUtility.initialize_database()

# call method to get application
app: Flask | None = UrlShortenerApplication.get_application()
