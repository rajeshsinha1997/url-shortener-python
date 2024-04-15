"""
Module: validation_utility

This module provides utility functions to validate application resources and return the
validation result if required. 
"""

from urllib.parse import ParseResult, urlparse
from loguru import logger

from app.constants.application_constant import ALLOWED_LOG_LEVELS


def is_valid_log_level(log_level: str | None) -> bool:
    """
    Checks if a given log level value is valid.

    Parameters:
    - log_level (str | None): value of the log level to be validated.

    Returns:
    - bool: True if the log level is valid, False otherwise.
    """
    return log_level is not None and log_level in ALLOWED_LOG_LEVELS


def is_valid_url(input_url: str) -> bool:
    """
    Check if the given string is a valid URL or not.

    Args:
    - input_url (str): The string to check.

    Returns:
    - bool: True if the string is a valid URL, False otherwise.
    """

    # parse the given string as an url
    logger.debug(f'parsing the given URL - {input_url}')
    __parsed_url: ParseResult = urlparse(url=input_url)

    # validate and return result
    logger.debug(f'validating the parsed URL - {input_url}')
    return all([__parsed_url.scheme, __parsed_url.netloc])
