"""
Module: validation_utility

This module provides utility functions to validate application resources and return the
validation result if required. 
"""

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
