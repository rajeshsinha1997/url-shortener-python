"""
Module: url_shortener_service

This module provides necessary service functions, which are responsible to execute the required
business logics for the url shortening service.
"""


import os
import random
import uuid

from app.models.db.database_model import UrlData
from app.repositories.url_shortener_repository import \
    add_shortened_url_record, find_short_url_value_by_long_url_hash
from app.utilities.common_utility import generate_hash_from_string, get_current_time_stamp


def __generate_shortened_url(length: int) -> str:
    """
    Generate a shortened URL by combining random characters from a UUID string
    with the current date in the format DDMMYY.

    Args:
        length (int): The length of the random string to generate.

    Returns:
        str: The shortened URL composed of random characters and the current date.
    """

    # generate a random uuid string and remove hyphens
    __uuid_string: str = str(object=uuid.uuid4()).replace('-', '')

    # select any random 7 characters from the uuid string
    __random_string: str = ''.join(random.sample(
        population=__uuid_string,
        k=length))

    # get the current date in the format DDMMYY (Day-Month-Year)
    __current_date: str = get_current_time_stamp(output_format='%d%m%y')

    # combine the random string and current date to create the shortened URL
    __shortened_url: str = f"{__random_string}{__current_date}"

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
    __long_url_hash: str = generate_hash_from_string(input_string=long_url)

    # find an existing short url for the given long url
    __existing_short_url: str | None = find_short_url_value_by_long_url_hash(
        long_url_hash=__long_url_hash
        )

    # check if any existing short url was found
    if __existing_short_url is not None:
        # return the existing short url
        return __existing_short_url

    # get required length of the shortened url
    __short_url_length: str = os.environ.get('SHORT_URL_STRING_LENGTH') or '7'

    # generate shortened url for the given long url
    __shortened_url: str = __generate_shortened_url(length=int(__short_url_length))

    # add generated shortened url data to the database
    add_shortened_url_record(record_to_add=UrlData(
        short_url=__shortened_url,
        long_url=long_url,
        long_url_hash=__long_url_hash,
        created_on=get_current_time_stamp(),
        last_used_on=get_current_time_stamp(),
    ))

    # return generated shortened url
    return __shortened_url
