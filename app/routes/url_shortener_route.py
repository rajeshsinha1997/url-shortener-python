"""
Module: url_shortener_route

This module defines a Flask Blueprint for handling endpoints related to the functionalities
such as shortening a long url, retrieving the original long url from the shortened url
"""


from flask import Blueprint, Response, request
from loguru import logger
from sqlalchemy.exc import DBAPIError

from app.interfaces.services.url_shortener_service_interface import IUrlShortenerService
from app.utilities.common_utility import build_response, get_json_request_body
from app.utilities.validation_utility import is_valid_url


class UrlShortenerBlueprint(Blueprint):
    """
    Blueprint for URL shortener API endpoints.

    This blueprint defines the URL shortener API endpoints and their corresponding handlers.
    """

    def __init__(self,
                 name: str,
                 import_name: str,
                 url_prefix: str,
                 url_shortener_service: IUrlShortenerService) -> None:
        """
        Initializes the URL shortener blueprint with the specified parameters.

        Parameters:
            name (str): The name of the blueprint.
            import_name (str): The import name of the blueprint.
            url_prefix (str): The URL prefix for the blueprint.
            url_shortener_service (IUrlShortenerService): The URL shortener service 
            associated with the blueprint.

        Returns:
            None
        """

        # call super class constructor
        super().__init__(name=name, import_name=import_name, url_prefix=url_prefix)

        # add service reference
        self.url_shortener_service: IUrlShortenerService = url_shortener_service

        # add url rule
        self.add_url_rule(rule='/shorten/',
                          view_func=self.generate_shortened_url)

    def generate_shortened_url(self) -> Response:
        """
        Handler for the POST /api/shorten/ endpoint

        Returns:
            Response: HTTP response containing the shortened URL value.
        """

        # log request
        logger.info(f'received {request.method} request to {request.url}' +
                    f'with payload - {request.data.decode()}')

        # validate and extract json request body from flask HTTP request
        __request_body: dict[str, object] | None = get_json_request_body(
            request=request)
        logger.debug(f'received JSON request body - {__request_body}')

        # check if request body is not a valid json request body
        if __request_body is None:
            # send corresponding error response
            logger.error(
                'a valid JSON request body was not found with the request')
            return build_response(response_data='A VALID JSON REQUEST BODY WAS NOT FOUND',
                                  response_status_code=400)

        # fetch required data from the request body
        __long_url: object | None = __request_body.get('long-url')
        logger.info(
            f'retrieved long URL from JSON request body - {__long_url}')

        # check if the required data was not found in the request body
        if __long_url is None:
            # send corresponding error response
            logger.error('no long URL data was found in the JSON request body')
            return build_response(
                response_data='REQUIRED LONG URL WAS NOT FOUND IN THE REQUEST BODY',
                response_status_code=400)

        # check if the received data is not a valid url
        if not is_valid_url(input_url=str(object=__long_url)):
            # send corresponding error response
            logger.error(
                f'retrieved value of the long URL is not a valid URL - {__long_url}')
            return build_response(response_data=f'INVALID LONG URL: {__long_url}',
                                  response_status_code=400)

        try:
            # call service function to get the shortened URL and build the response
            logger.debug(
                f'creating short URL from the given long URL - {__long_url}')
            return build_response(
                response_data=self.url_shortener_service.create_short_url_from_long_url(
                    long_url=str(object=__long_url)),
                response_status_code=201)
        except (FileNotFoundError, DBAPIError) as __e:
            # return corresponding error response
            logger.error(f'error - {__e}')
            return build_response(response_data='SOME INTERNAL ERROR OCCURRED',
                                  response_status_code=500)
