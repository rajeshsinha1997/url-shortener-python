"""
Module: common_utility

This module provides utility functions for common tasks across the application.
"""

from datetime import datetime
from hashlib import sha512
import json
import os

from flask import Request, Response
from app.exceptions.custom_application_exceptions import QueryFileNotFoundException
from app.models.api.response_model import ApplicationResponse
from app.utilities.validation_utility import does_request_has_json_body


def get_current_time_stamp(output_format: str ='%Y/%m/%dT%H:%M:%S:%f') -> str:
    """
    Get the current timestamp in a specified format.

    Args:
        output_format (str, optional): The format string used to represent the timestamp.
            Defaults to '%Y/%m/%dT%H:%M:%S:%f'.

    Returns:
        str: The current timestamp formatted according to the provided format string.
    """

    # return the formatted current datetime
    return datetime.now().strftime(format=output_format)


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


def get_json_request_body(request: Request) -> dict[str, str] | None:
    """
    Retrieves the JSON request body from a Flask HTTP request object.

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


def generate_hashed_value_from_string(source: str, hash_length: int | None = None) -> str:
    """
    Generate a hashed value from a given string
    
    Parameters:
        source (str): The source string value which will be hashed
        hash_length (int | None): required length of the hashed representation of the given string

    Returns:
        str: hashed representation as string of the given string value truncated to the required
        length value provided, if no length value is provided then the complete hashed
        representation is returned as a string.
    """

    # encode the given string
    __encoded_string: bytes = source.encode(encoding='UTF-8', errors='ignore')

    # create hash object of the given string value
    __hash_obj: object = sha512()

    # update the hash object with the encoded string value
    __hash_obj.update(__encoded_string)

    # retrieve the hashed representation as string from the hash object
    __hashed_value: str = __hash_obj.hexdigest()

    # check if any length value has been provided and it is a valid length value
    if hash_length is not None and 0 < hash_length < 128:
        # truncate the hashed string to the required length and return the value
        return __hashed_value[:hash_length]
    # else return the complete hashed representation of the given string value
    return __hashed_value


def get_sql_query_from_file(file_path: str) -> str:
    """
    Get SQL query from a file.

    Parameters:
        file_path (str): The path to the file containing SQL query.

    Returns:
        str: The SQL query retrieved from the file.

    Raises:
        QueryFileNotFoundException: If the provided file path does not exist.
    """

    # check if the provided file path exists
    if os.path.exists(path=file_path):
        # open file present at the provided path in reading mode
        with open(file=file_path, mode='r', encoding='UTF-8') as query:
            # return the contents of the file into a variable
            return query.read()
    # else throw corresponding error
    else:
        raise QueryFileNotFoundException(
            exception_message=f'INVALID SQL QUERY FILE PATH: {file_path}')
