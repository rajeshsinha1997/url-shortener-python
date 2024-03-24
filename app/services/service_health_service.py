from app.constants.application_constant import APPLICATION_NAME
from app.constants.application_constant import APPLICATION_STATUS_UP
from app.models.api.response_model import ServiceHealthResponse
from app.utilities.common_utility import get_current_time_stamp


class ServiceHealthService:

    # method to build service-health response
    @classmethod
    def build_service_health_response(cls) -> ServiceHealthResponse:
        # build service health response object
        service_health_response = ServiceHealthResponse(
            current_timestamp=get_current_time_stamp(),
            application_name=APPLICATION_NAME,
            application_status=APPLICATION_STATUS_UP,
            connected_service_healths=[]
            )

        # add service-health data of connected services

        # return service-health response
        return service_health_response
