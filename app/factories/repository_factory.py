from sqlalchemy import Engine
from app.interfaces.repositories.health_repository_interface import IHealthRepository
from app.repositories.health_repository_postgresql import HealthRepositoryPostgreSQLImpl


class RepositoryFactory:

    __health_repository: IHealthRepository | None = None

    @classmethod
    def get_health_repository(cls, database_engine: Engine) -> IHealthRepository:
        """
        method
        """
        if cls.__health_repository is None:
            cls.__health_repository = HealthRepositoryPostgreSQLImpl(
                engine=database_engine)

        return cls.__health_repository
