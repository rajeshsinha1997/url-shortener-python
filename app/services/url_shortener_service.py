"""
Module: url_shortener_service

This module provides necessary service functions, which are responsible to execute the required
business logics for the url shortening service.
"""


import os
import random
import uuid

from loguru import logger

from app.models.database_model import UrlData
from app.repositories.url_shortener_repository import \
    add_shortened_url_record, find_short_url_value_by_long_url_hash
from app.utilities.common_utility import generate_hash_from_string, get_current_time_stamp


def __generate_shortened_url(length: int) -> str:
    """
    Generate a shortened URL by combining random characters from a UUID string
    with the current date in the format DDMMYY.

    Parameters:
        length (int): The length of the random string to generate.

    Returns:
        str: The shortened URL composed of random characters and the current date.
    """

    # generate a random uuid string and remove hyphens
    __uuid_string: str = str(object=uuid.uuid4()).replace('-', '')
    logger.debug(f'generated random UUID v4 string - {__uuid_string}')

    # select any random characters for a specific count from the uuid string
    __random_string: str = ''.join(random.sample(
        population=__uuid_string,
        k=length))
    logger.debug(f'generated short URL string - {__random_string}')

    # get the current date in the format DDMMYY (Day-Month-Year)
    __current_date: str = get_current_time_stamp(output_format='%d%m%y')

    # combine the random string and current date to create the shortened URL
    __shortened_url: str = f"{__random_string}{__current_date}"
    logger.info(f'generated short URL - {__shortened_url}')

    # return the shortened URL
    return __shortened_url


def create_short_url_from_long_url(long_url: str) -> str:
    """
    Create a shortened URL from the provided long URL value

    Parameters:
        long_url (str): the long URL required to be shortened

    Returns:
        str: shortened version of the provided long URL as string
    """

    # generate hash of the given long url
    logger.info(f'generating hash for the long URL - {long_url}')
    __long_url_hash: str = generate_hash_from_string(
        input_string=long_url,
        algorithm=os.environ.get('LONG_URL_HASH_ALGORITHM') or 'md5')

    # find an existing short url for the given long url
    logger.info(
        f'checking if the long URL has been shortened before - {long_url}')
    __existing_short_url: str | None = find_short_url_value_by_long_url_hash(
        long_url_hash=__long_url_hash
    )

    # check if any existing short url was found
    if __existing_short_url is not None:
        # return the existing short url
        logger.info(f'short URL \'{__existing_short_url}\' ' +
                    f'already exists for the long URL - {long_url}')
        return __existing_short_url

    # get required length of the shortened url
    __short_url_length: str | None = os.environ.get('SHORT_URL_STRING_LENGTH')
    logger.debug('retrieved value of the short URL string length ' +
                 f'from the environment - {__short_url_length}')

    # generate shortened url for the given long url
    __shortened_url: str = __generate_shortened_url(
        length=int(__short_url_length or '7'))
    logger.info(f'short URL \'{
                __shortened_url}\' generated for the long URL - {long_url}')

    # add generated shortened url data to the database
    add_shortened_url_record(record_to_add=UrlData(
        params={
            'short_url': __shortened_url,
            'long_url': long_url,
            'long_url_hash': __long_url_hash,
            'created_on': get_current_time_stamp(),
            'last_used_on': get_current_time_stamp(),
        }))
    logger.info(f'saved new short URL \'{
                __shortened_url}\' for the long URL - {long_url}')

    # return generated shortened url
    return __shortened_url
