"""
Module: constants

This module defines constant values to be used across the URL shortener application.
"""

from typing import List


# application related constants values
APPLICATION_NAME: str = 'URL-SHORTENER-REST-API'
APPLICATION_STATUS_UP: str = 'UP'
APPLICATION_STATUS_DOWN: str = 'DOWN'


# logging related constant values
ALLOWED_LOG_LEVELS: List[str] = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
DEFAULT_LOG_LEVEL: str = 'INFO'
LOG_OUTPUT_FILE_PATH: str = 'logs/usra.log'
LOG_OUTPUT_FILE_ROTATION_SIZE: str = '500 MB'
