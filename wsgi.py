"""
Module: main

This module serves as the entry point for the URL shortener application.
It initializes the Flask application and retrieves the application instance
from the UrlShortenerApplication class.
"""

import os
from dotenv import load_dotenv
from flask import Flask
from app.app import UrlShortenerApplication

# check if the current environment is not 'production'
if os.getenv(key='environment') != 'production':
    # load dotenv file
    load_dotenv()

# call method to get application
app: Flask | None = UrlShortenerApplication.get_application()
