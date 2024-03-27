"""
Module: common_utility

This module provides utility functions for common tasks across the application.
"""

from datetime import datetime
import json

from flask import Request, Response
from app.models.api.response_model import ApplicationResponse
from app.utilities.validation_utility import does_request_has_json_body


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
    __application_response = ApplicationResponse(
                        current_timestamp=get_current_time_stamp(),
                        response_data=response_data)

    # create json representation of the application response
    __json_response: str = json.dumps(obj=__application_response,
                                    default=lambda obj: obj.to_json(),
                                    indent=4)

    # return response object with response data
    return Response(content_type='application/json',
                    status=response_status_code,
                    response=__json_response)


def validate_and_get_json_request_body(request: Request) -> dict[str, str] | None:
    """
    Validates and retrieves the JSON request body from a Flask HTTP request object.

    Args:
        request (Request): The Flask HTTP request object.

    Returns:
        dict[str, str] | None: A dictionary representing the JSON request body if the request
        is valid and contains JSON data. Otherwise, returns None.
    """

    # check if flask HTTP request contains a valid json request body
    if does_request_has_json_body(request=request):
        # get json request body from flask HTTP request object
        __json_request_body: dict[str, str] | None = request.get_json(silent=True)

        # check if a valid json request body was parsed and contains at least a single entry
        if __json_request_body is not None and len(__json_request_body.keys()) > 0:
            # return parsed json request body
            return __json_request_body
        # else return None as result
        return None

    # else return None as fallback result
    return None
