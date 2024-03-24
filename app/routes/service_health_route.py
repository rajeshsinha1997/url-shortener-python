from flask import Blueprint, Response

from app.services.service_health_service import ServiceHealthService
from app.utilities.common_utility import build_response

# create blueprint
service_health_blueprint = Blueprint(name='health',
                                     import_name=__name__,
                                     url_prefix='/health/')


# define GET endpoint
@service_health_blueprint.get(rule='/')
def get_service_health() -> Response:
    # return service health response
    return build_response(
        response_data=ServiceHealthService.build_service_health_response(),
        response_status_code=200)
