from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='DB_')

    HOST: str
    PORT: int
    NAME: str
    USER: str
    PASSWORD: str


db_settings = DBSettings()
