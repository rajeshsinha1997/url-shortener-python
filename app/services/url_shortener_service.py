"""
Module: url_shortener_service

This module provides necessary service functions, which are responsible to execute the required
business logics for the url shortening service.
"""


import os
from app.models.db.database_model import UrlDatabaseRecord
from app.repositories.url_shortener_repository import \
    add_shortened_url_record, find_record_by_long_url
from app.utilities.common_utility import generate_hashed_value_from_string, get_current_time_stamp


def create_short_url_from_long_url(long_url: str) -> str:
    """
    Create a shortened URL from the provided long URL value

    Parameters:
        long_url: long URL required to be shortened

    Returns:
        shortened version of the provided long URL as string
    """

    # find an existing record corresponding to the given long URL
    __existing_record: UrlDatabaseRecord | None = find_record_by_long_url(long_url=long_url)

    # check if an existing record was not found
    if __existing_record is None:
        # get the environment variable value for the hash length
        __hash_length: str = os.environ.get('HASH_LENGTH') or '20'

        # generate shortened url from the provided long url
        __short_url: str = generate_hashed_value_from_string(source=long_url[::-1],
                                                        hash_length=int(__hash_length))

        # store the shortened url to database
        add_shortened_url_record(record_to_add=UrlDatabaseRecord(
            short_url=__short_url,
            long_url=long_url,
            deleted=False,
            created_on=get_current_time_stamp()))

        # return the generated shortened url
        return __short_url

    # check if the existing record has been deleted already
    if __existing_record.deleted:
        # mark the existing record as not deleted
        __existing_record.deleted = False

        # make update on the database

    # return the existing shortened url
    return __existing_record.short_url
