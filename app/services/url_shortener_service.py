"""
Module: url_shortener_service

This module provides necessary service functions, which are responsible to execute the required
business logics for the url shortening service.
"""


from app.repositories.url_shortener_repository import find_shortened_url_by_long_url


def create_short_url_from_long_url(long_url: str) -> str:
    """
    Create a shortened URL from the provided long URL value

    Parameters:
        long_url: long URL required to be shortened

    Returns:
        shortened version of the provided long URL as string
    """

    # find an existing shortened URL corresponding to the given long URL
    __short_url: str | None = find_shortened_url_by_long_url(long_url=long_url)

    # check if an existing shortened URL was found
    if __short_url is not None:
        # return the existing shortened url
        return __short_url

    # else create a shortened version of the given long URL
    return 'OK'
