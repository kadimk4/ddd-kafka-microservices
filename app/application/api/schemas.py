from pydantic import BaseModel


class BadRequestSchema(BaseModel):
    request: str