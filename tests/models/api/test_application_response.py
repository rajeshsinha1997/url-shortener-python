"""
This module contains test functions which are responsible to perform unit testing
on the ApplicationResponse class
"""
from app.models.response_model import ApplicationResponse


def test_application_response_json() -> None:
    """
    tests the JSON representation of an instance of ApplicationResponse
    """
    # create instance of ApplicationResponse to test
    __application_response = ApplicationResponse(
        current_timestamp='demo-timestamp', response_data='demo-data')

    # create expected json representation
    __expected: dict[str, object] = {
        'response-timestamp': 'demo-timestamp', 'response-data': 'demo-data'}

    # test with the actual data
    assert __application_response.to_json() == __expected


def test_application_response_string() -> None:
    """
    tests the string representation of an instance of ApplicationResponse
    """
    # create instance of ApplicationResponse to test
    __application_response = ApplicationResponse(
        current_timestamp='demo-timestamp', response_data='demo-data')

    # create expected string representation
    __expected: str = str(object={
        'response-timestamp': 'demo-timestamp', 'response-data': 'demo-data'})

    # test with the actual data
    assert str(object=__application_response) == __expected
