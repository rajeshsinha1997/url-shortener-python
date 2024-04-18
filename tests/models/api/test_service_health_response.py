"""
This module contains test functions which are responsible to perform unit testing
on the ServiceHealthResponse class
"""
from app.models.api.response_model import ServiceHealthResponse


def test_service_health_response_json_no_connected_service() -> None:
    """
    test the JSON representation of an instance of ServiceHealthResponse
    """
    # create instance of ServiceHealthResponse to test
    __service_health_response = ServiceHealthResponse(params={
        'current_timestamp': 'test timestamp',
        'application_name': 'test application',
        'application_version': 'test-version',
        'application_status': 'test-status'
    })

    # create expected JSON representation
    __expected: dict[str, object] = {
        'health-check-timestamp': 'test timestamp',
        'application-name': 'test application',
        'application_version': 'test-version',
        'application-status': 'test-status',
        'connected-services-health': []
    }

    # test against the actual data
    assert __service_health_response.to_json() == __expected


def test_service_health_response_string_no_connected_service() -> None:
    """
    test the string representation of an instance of ServiceHealthResponse
    """
    # create instance of ServiceHealthResponse to test
    __service_health_response = ServiceHealthResponse(params={
        'current_timestamp': 'test timestamp',
        'application_name': 'test application',
        'application_version': 'test-version',
        'application_status': 'test-status'
    })

    # create expected string representation
    __expected: str = str(object={
        'health-check-timestamp': 'test timestamp',
        'application-name': 'test application',
        'application_version': 'test-version',
        'application-status': 'test-status',
        'connected-services-health': []
    })

    # test against the actual data
    assert str(object=__service_health_response) == __expected


def test_service_health_response_json() -> None:
    """
    test the JSON representation of an instance of ServiceHealthResponse
    with a connected service data present
    """
    # create instance of ServiceHealthResponse to test
    __service_health_response = ServiceHealthResponse(params={
        'current_timestamp': 'test timestamp',
        'application_name': 'test application',
        'application_version': 'test-version',
        'application_status': 'test-status'
    })

    # add connected service data
    __service_health_response.connected_services_health.append(
        ServiceHealthResponse(params={
            'current_timestamp': 'test timestamp 2',
            'application_name': 'test application 2',
            'application_version': 'test-version 2',
            'application_status': 'test-status 2'
        }))

    # create expected JSON representation
    __expected: dict[str, object] = {
        'health-check-timestamp': 'test timestamp',
        'application-name': 'test application',
        'application_version': 'test-version',
        'application-status': 'test-status',
        'connected-services-health': [{
            'health-check-timestamp': 'test timestamp 2',
            'application-name': 'test application 2',
            'application_version': 'test-version 2',
            'application-status': 'test-status 2',
            'connected-services-health': []
        }]
    }

    # test against the actual data
    assert __service_health_response.to_json() == __expected


def test_service_health_response_string() -> None:
    """
    test the string representation of an instance of ServiceHealthResponse
    """
    # create instance of ServiceHealthResponse to test
    __service_health_response = ServiceHealthResponse(params={
        'current_timestamp': 'test timestamp',
        'application_name': 'test application',
        'application_version': 'test-version',
        'application_status': 'test-status'
    })

    # add connected service data
    __service_health_response.connected_services_health.append(
        ServiceHealthResponse(params={
            'current_timestamp': 'test timestamp 2',
            'application_name': 'test application 2',
            'application_version': 'test-version 2',
            'application_status': 'test-status 2'
        }))

    # prepare expected data object
    __expected: dict[str, object] = {
        'health-check-timestamp': 'test timestamp',
        'application-name': 'test application',
        'application_version': 'test-version',
        'application-status': 'test-status',
        'connected-services-health': [{
            'health-check-timestamp': 'test timestamp 2',
            'application-name': 'test application 2',
            'application_version': 'test-version 2',
            'application-status': 'test-status 2',
            'connected-services-health': []
        }]
    }

    # test against the actual data
    assert str(object=__service_health_response) == str(object=__expected)
