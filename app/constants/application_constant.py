"""
Module: constants

This module defines constant values to be used across the URL shortener application.
"""

from typing import List

from app.utilities.common_utility import get_current_time_stamp


# application related constants values
APPLICATION_NAME: str = 'URL-SHORTENER-REST-API'
APPLICATION_STATUS_UP: str = 'UP'
APPLICATION_STATUS_DOWN: str = 'DOWN'


# database related constant values
ALLOWED_ECHO_VALUES = ['True', 'False']


# logging related constant values
ALLOWED_LOG_LEVELS: List[str] = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
DEFAULT_LOG_LEVEL: str = 'INFO'
LOG_OUTPUT_FILE_PATH: str = f'logs/{get_current_time_stamp(output_format='%Y_%m_%d')}.log'
LOG_OUTPUT_FILE_ROTATION_SIZE: str = '500 MB'
