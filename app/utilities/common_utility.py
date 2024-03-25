"""
Module: common_utility

This module provides utility functions for common tasks such as retrieving 
the current timestamp and building HTTP responses.
"""

from datetime import datetime
import json

from flask import Response
from app.models.api.response_model import ApplicationResponse


def get_current_time_stamp() -> str:
    """
    Retrieve the current timestamp in a formatted string.

    Returns:
        str: The formatted current timestamp.
    """

    # return the formatted current datetime
    return datetime.now().strftime('%Y/%m/%dT%H:%M:%S:%f')


def build_response(response_data: object,
                   response_status_code: int) -> Response:
    """
    Build a Flask response object with the given response data and status code.

    Args:
        response_data (object): The data to include in the response.
        response_status_code (int): The HTTP status code for the response.

    Returns:
        Response: The Flask response object.
    """

    # build application response
    application_response = ApplicationResponse(
                        current_timestamp=get_current_time_stamp(),
                        response_data=response_data)

    # create json representation of the application response
    json_response: str = json.dumps(obj=application_response,
                                    default=lambda obj: obj.to_json(),
                                    indent=4)

    # return response object with response data
    return Response(content_type='application/json',
                    status=response_status_code,
                    response=json_response)
