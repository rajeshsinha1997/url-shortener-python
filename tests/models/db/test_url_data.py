"""
This module contains test functions which are responsible to perform unit testing
on the UrlData class
"""
from app.models.db.database_model import UrlData


def test_url_data_string() -> None:
    """
    test the string representation of an instance of UrlData
    """
    # create instance of UrlData to test
    __url_data = UrlData(params={
        'short_url': 'test short url',
        'long_url': 'test long url',
        'long_url_hash': 'test long url hash',
        'created_on': 'test created on',
        'last_used_on': 'test last used on'
    })

    # create expected string representation
    __expected: str = 'Short URL: test short url, '\
        'Long URL: test long url, Long URL Hash: test long url hash, '\
        'Created On: test created on, Last Used On: test last used on'

    # test against the actual data
    assert str(object=__url_data) == __expected
