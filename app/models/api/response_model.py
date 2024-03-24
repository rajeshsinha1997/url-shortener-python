# model class representing structure of a response
class ApplicationResponse:

    # define constructor
    def __init__(self,
                 current_timestamp: str,
                 response_data: object) -> None:
        self.response_timestamp: str = current_timestamp
        self.response_data: object = response_data

    # method to get a json representation of this object
    def to_json(self) -> dict[str, str | object]:
        return {
            'response-timestamp': self.response_timestamp,
            'response-data': self.response_data
            }


# model class representing structure of a service-health response
class ServiceHealthResponse:

    # define constructor
    def __init__(self,
                 current_timestamp: str,
                 application_name: str,
                 application_status: str,
                 connected_service_healths: list['ServiceHealthResponse']
                 ) -> None:
        self.health_check_timestamp: str = current_timestamp
        self.application_name: str = application_name
        self.application_status: str = application_status
        self.connected_service_healths: list[
            'ServiceHealthResponse'] = connected_service_healths

    # method to get a json representation of this object
    def to_json(self) -> dict[str, str | object]:
        return {
            'health-check-timestamp': self.health_check_timestamp,
            'application-name': self.application_name,
            'application-status': self.application_status,
            'connected-service-health': [connected_service_health.to_json()
                                         for connected_service_health in
                                         self.connected_service_healths
                                         ]
        }
