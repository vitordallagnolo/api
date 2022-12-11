from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações Gerais
    """
    API_VI_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://dbuser:password@localhost:5432/faculdade"
    DBBaseModel = declarative_base()

    class Conmfig:
        case_sensitive = True




settings = Settings()