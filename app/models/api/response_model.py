"""
Module: response_models

This module defines model classes representing different types of responses used in the
URL shortener application.
"""


class ApplicationResponse:
    """
    Model class representing the structure of a generic response.
    """

    def __init__(self,
                 current_timestamp: str,
                 response_data: object) -> None:
        """
        Constructor for the ApplicationResponse class.

        Args:
            current_timestamp (str): The timestamp of the response.
            response_data (object): The data contained in the response.

        Returns:
            None

        """

        self.response_timestamp: str = current_timestamp
        self.response_data: object = response_data

    def to_json(self) -> dict[str, str | object]:
        """
        Create a JSON representation of an instance of this class.

        Returns:
            dict[str, str | object]: A dictionary containing the JSON representation of the
            instance.
        """

        # return the json representation of the instance
        return {
            'response-timestamp': self.response_timestamp,
            'response-data': self.response_data
        }

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """

        return str(object=self.to_json())


class ServiceHealthResponse:
    """
        Model class representing the structure of a service health response.
    """

    def __init__(self,
                 params: dict[str, str],
                 ) -> None:
        """
        Constructor for the ServiceHealthResponse class.

        Parameters:
            params (dict): A dictionary containing the following key-value pairs:
                - 'current_timestamp' (str): The timestamp of the health check.
                - 'application_name' (str): The name of the application.
                - 'application_version' (str): The current version of the application.
                - 'application_status' (str): The status of the application.

        Returns:
            None
        """

        self.health_check_timestamp: str = params['current_timestamp']
        self.application_name: str = params['application_name']
        self.application_version: str = params['application_version']
        self.application_status: str = params['application_status']
        self.connected_services_health: list['ServiceHealthResponse'] = []

    def to_json(self) -> dict[str, object]:
        """
        Create a JSON representation of an instance of this class.

        Returns:
            dict[str, object]: A dictionary containing the JSON representation of the
            instance.

        """

        # return the json representation of the instance
        return {
            'health-check-timestamp': self.health_check_timestamp,
            'application-name': self.application_name,
            'application_version': self.application_version,
            'application-status': self.application_status,
            'connected-services-health': [connected_service_health.to_json()
                                          for connected_service_health in
                                          self.connected_services_health]
        }

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """

        return str(object=self.to_json())
