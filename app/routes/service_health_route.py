from flask import Blueprint

# create blueprint
service_health_blueprint = Blueprint(name='health',
                                     import_name=__name__,
                                     url_prefix='/health')


# define GET endpoint
@service_health_blueprint.get(rule='/')
def get_service_health():
    return 'OK'
