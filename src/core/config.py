from pydantic.v1 import BaseSettings
from fastapi.templating import Jinja2Templates


class Settings(BaseSettings):
    TEMPLATES = Jinja2Templates(directory="templates")
    
    class Config:
        case_sensitive = True


settings: Settings = Settings()
