"""
Module: url_shortener_route

This module defines a Flask Blueprint for handling endpoints related to the functionalities
such as shortening a long url, retrieving the original long url from the shortened url
"""


from flask import Blueprint, Response, request
from sqlalchemy.exc import DBAPIError

from app.services.url_shortener_service import create_short_url_from_long_url
from app.utilities.common_utility import build_response, get_json_request_body
from app.exceptions.custom_application_exceptions import \
    DatabaseEngineNotInitializedException, QueryFileNotFoundException
from app.utilities.validation_utility import is_valid_url

# create blueprint
url_shortener_blueprint: Blueprint = Blueprint(name='url_shortener',
                                    import_name=__name__,
                                    url_prefix='/api/')


@url_shortener_blueprint.post(rule='/shorten/')
def generate_shortened_url() -> Response:
    """
    Handler for the POST /api/shorten/ endpoint

    Returns:
        Response: HTTP response containing the shortened URL value.
    """

    # validate and extract json request body from flask HTTP request
    __request_body: dict[str, str] | None = get_json_request_body(request=request)

    # check if request body is not a valid json request body
    if __request_body is None:
        # send corresponding error response
        return build_response(response_data='A VALID JSON REQUEST BODY WAS NOT FOUND',
                              response_status_code=400)

    # fetch required data from the request body
    __long_url: str | None = __request_body.get('long-url')

    # check if the required data was not found in the request body
    if __long_url is None:
        # send corresponding error response
        return build_response(response_data='REQUIRED LONG URL WAS NOT FOUND IN THE REQUEST BODY',
                              response_status_code=400)

    # check if the received data is not a valid url
    if not is_valid_url(input_url=__long_url):
        # send corresponding error response
        return build_response(response_data=f'INVALID LONG URL: {__long_url}',
                              response_status_code=400)

    try:
        # call service function to get the shortened URL and build the response
        return build_response(response_data=create_short_url_from_long_url(long_url=__long_url),
                              response_status_code=201)
    except (QueryFileNotFoundException, DatabaseEngineNotInitializedException, DBAPIError):
        # return corresponding error response
        return build_response(response_data='SOME INTERNAL ERROR OCCURRED',
                              response_status_code=500)
