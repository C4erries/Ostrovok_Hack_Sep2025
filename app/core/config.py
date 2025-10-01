from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_v1_prefix: str = Field(default="/api/v1")
    project_name: str = Field(default="Островок альфа")
    secret_key: str = Field(default="supersecret")
    access_token_expire_minutes: int = Field(default=60)
    algorithm: str = Field(default="HS256")
    database_url: str = Field(default="sqlite:///./app.db")
    static_root: str = Field(default="static")
    static_url: str = Field(default="/static")
    application_photos_prefix: str = Field(default="applications")
    report_photos_prefix: str = Field(default="reports")

    class Config:
        env_file = ".env"


settings = Settings()
