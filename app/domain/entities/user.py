
from dataclasses import dataclass


from app.domain.entities.base import BaseEntity
from app.domain.values.email import EmailStr


@dataclass(eq=False, kw_only=True)
class User(BaseEntity):
    username: str
    email: EmailStr

