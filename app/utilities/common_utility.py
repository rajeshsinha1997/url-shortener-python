"""
Module: common_utility

This module provides utility functions for common tasks across the application.
"""

from datetime import datetime
from hashlib import new
import json
import os

from flask import Request, Response
from loguru import logger
from app.exceptions.custom_application_exceptions import QueryFileNotFoundException
from app.models.api.response_model import ApplicationResponse


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
    logger.debug(f'returning the current timestamp in format - ${output_format}')
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

    # build application response object
    logger.debug(f'building response object with response data - {response_data}')
    __application_response = ApplicationResponse(
                        current_timestamp=get_current_time_stamp(),
                        response_data=response_data)

    # create json representation of the application response object
    logger.debug(f'creating a JSON representation of the response - {__application_response}')
    __json_response: str = json.dumps(obj=__application_response,
                                    default=lambda obj: obj.to_json(),
                                    indent=4)

    # return response object with response data
    logger.info(f'returning response with response status code - {response_status_code}, '+
                f'response data - {__json_response}')
    return Response(content_type='application/json',
                    status=response_status_code,
                    response=__json_response)


def get_json_request_body(request: Request) -> dict[str, object] | None:
    """
    Retrieves the JSON request body from a Flask HTTP request object.

    Args:
        request (Request): The Flask HTTP request object.

    Returns:
        dict[str, object] | None: A dictionary representing the JSON request body if the request
        is valid and contains JSON data. Otherwise, returns None.
    """

    # check if flask HTTP request contains a valid json request body
    logger.debug('verifying if the request contains a JSON body')
    if request.is_json:
        # get json request body from flask HTTP request object
        logger.debug('retrieving the JSON body from the request')
        __json_request_body: dict[str, object] | None = request.get_json(silent=True)

        # check if a valid json request body was parsed and contains at least a single entry
        logger.debug('verifying if the JSON request body contains at least one record')
        if __json_request_body is not None and len(__json_request_body.keys()) > 0:
            # return parsed json request body
            return __json_request_body

        # else return None as result
        logger.warning('JSON request body doesn\'t contain any record')
        return None

    # else return None as fallback result
    logger.warning('request doesn\'t contain any JSON body')
    return None


def generate_hash_from_string(input_string: str, algorithm: str='sha256') -> str:
    """
    Generate the hash of a given string using the specified algorithm.

    Args:
    - input_string (str): The string to generate the hash for.
    - algorithm (str): The hash algorithm to use (default is 'sha256').
                       Other options include 'md5', 'sha1', 'sha224', 'sha256',
                       'sha384', 'sha512', depending on hashlib supported algorithms.

    Returns:
    - str: The hash of the input string.
    """

    # declare hash object
    __hash_object: object | None = None

    try:
        # initialize the hash object using the specified algorithm
        logger.debug(f'trying to create hash object with algorithm - {algorithm}')
        __hash_object = new(name=algorithm)
    except ValueError:
        # initialize the hash object using the default algorithm
        logger.debug('trying to create hash object with algorithm - sha256')
        __hash_object = new(name='sha256')

    # update the hash object with the input string
    logger.debug('encoding the given string into the hash object created')
    __hash_object.update(input_string.encode())

    # generate and return hash in hexadecimal format
    logger.debug('converting hash value to a string in hexadecimal format')
    return __hash_object.hexdigest()


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
    logger.debug(f'checking if the given path to the sql file exists - {file_path}')
    if os.path.exists(path=file_path):
        # open file present at the provided path in reading mode
        logger.debug(f'opening the sql file at the given path in reading mode - {file_path}')
        with open(file=file_path, mode='r', encoding='UTF-8') as query:
            # return the contents of the file into a variable
            logger.debug(f'reading the contents of the sql file at the given path - {file_path}')
            return query.read()
    # else throw corresponding error
    else:
        logger.error(f'given path to the sql file is invalid - {file_path}')
        raise QueryFileNotFoundException(
            exception_message=f'INVALID SQL QUERY FILE PATH: {file_path}')
