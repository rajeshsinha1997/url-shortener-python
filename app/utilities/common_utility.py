from datetime import datetime
import json

from flask import Response
from app.models.api.response_model import ApplicationResponse


# method to get current timestamp
def get_current_time_stamp() -> str:
    # return the formatted current datetime
    return datetime.now().strftime('%Y/%m/%dT%H:%M:%S:%f')


# method to build a response object
def build_response(response_data: object,
                   response_status_code: int) -> Response:
    # build application response
    application_response = ApplicationResponse(
                        current_timestamp=get_current_time_stamp(),
                        response_data=response_data)

    # create json representation of the application response
    json_response: str = json.dumps(obj=application_response,
                                    default=lambda obj: obj.to_json(),
                                    indent=4)

    # return response object with response data
    return Response(content_type='application/json',
                    status=response_status_code,
                    response=json_response)
