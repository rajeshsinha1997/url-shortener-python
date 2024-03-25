"""
Module: response_models

This module defines model classes representing different types of responses 
used in the URL shortener application.
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
            dict[str, str | object]: A dictionary containing the JSON 
                                     representation of the instance.
        """

        # return the json representation of the instance
        return {
            'response-timestamp': self.response_timestamp,
            'response-data': self.response_data
            }


class ServiceHealthResponse:
    """
        Model class representing the structure of a service health response.
    """

    def __init__(self,
                 current_timestamp: str,
                 application_name: str,
                 application_status: str,
                 connected_services_health: list['ServiceHealthResponse']
                 ) -> None:
        """
        Constructor for the ServiceHealthResponse class.

        Args:
            current_timestamp (str): The timestamp of the health check.
            application_name (str): The name of the application.
            application_status (str): The status of the application.
            connected_services_health (list[ServiceHealthResponse]): 
                                    The health status of connected services.

        Returns:
            None
        """
        self.health_check_timestamp: str = current_timestamp
        self.application_name: str = application_name
        self.application_status: str = application_status
        self.connected_services_health: list[
            'ServiceHealthResponse'] = connected_services_health

    def to_json(self) -> dict[str, str | object]:
        """
        Create a JSON representation of an instance of this class.

        Returns:
            dict[str, str | object]: A dictionary containing the JSON 
                                     representation of the instance.

        """

        # return the json representation of the instance
        return {
            'health-check-timestamp': self.health_check_timestamp,
            'application-name': self.application_name,
            'application-status': self.application_status,
            'connected-services-health': [connected_service_health.to_json()
                                          for connected_service_health in
                                          self.connected_services_health]
        }
