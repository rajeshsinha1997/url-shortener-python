"""
Module: validation_utility

This module provides utility functions to validate application resources and return the
validation result if required. 
"""

from urllib.parse import ParseResult, urlparse
from flask import Request


def does_request_has_json_body(request: Request) -> bool:
    """
    Check if the flask HTTP request contains a valid json request body.
    
    Args:
        request (Request): The Flask HTTP request object.
    
    Returns: 
        True if the flask HTTP request contains a valid json request body, False otherwise.
    """
    return request.is_json


def is_valid_url(input_url: str) -> bool:
    """
    Check if the given string is a valid URL or not.

    Args:
    - input_url (str): The string to check.

    Returns:
    - bool: True if the string is a valid URL, False otherwise.
    """

    # parse the given string as an url
    __parsed_url: ParseResult = urlparse(url=input_url)

    # validate and return result
    return all([__parsed_url.scheme, __parsed_url.netloc])
