from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    mongodb_connection_uri: str = Field(alias="MONGODB_CONNETION_URI")
    mongodb_user_db: str = Field(alias="MONGODB_USER_DB")
    mongodb_user_collection: str = Field(alias="MONGODB_USER_COLLECTION")
