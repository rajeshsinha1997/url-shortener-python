from flask import Flask

from app.routes.service_health_route import service_health_blueprint


class UrlShortenerApplication:
    # define class level private variables
    __application: Flask | None = None

    # private class method to create the application
    @classmethod
    def __create_application(cls) -> None:
        # check if the application has not been created already
        if (cls.__application is None):
            # create flask application
            cls.__application = Flask(import_name=__name__)

            # register blueprints
            cls.__application.register_blueprint(
                blueprint=service_health_blueprint)

    # public class method to get the application
    @classmethod
    def get_application(cls) -> Flask | None:
        # check if the application has not been created
        if (cls.__application is None):
            # call method to create application
            cls.__create_application()

        # return application
        return cls.__application
