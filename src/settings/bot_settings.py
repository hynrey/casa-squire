from pydantic import Field
from pydantic_settings import BaseSettings


class BotSettings(BaseSettings):
    token: str = Field(validation_alias="TELEGRAM_BOT_TOKEN")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"
