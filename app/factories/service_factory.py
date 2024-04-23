from app.interfaces.repositories.health_repository_interface import IHealthRepository
from app.interfaces.services.health_service_interface import IHealthService
from app.services.health_service import HealthServiceImpl


class ServiceFactory:
    """
    Class
    """
    __health_service: IHealthService | None

    @classmethod
    def get_health_service(cls, health_repository: IHealthRepository) -> IHealthService:
        """
        method
        """
        if cls.__health_service is None:
            cls.__health_service = HealthServiceImpl(
                health_repository=health_repository)

        return cls.__health_service
