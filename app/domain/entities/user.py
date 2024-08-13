from dataclasses import dataclass

from domain.entities.base import BaseEntity
from domain.values.email import Email


@dataclass(eq=False, kw_only=True)
class User(BaseEntity):
    username: str
    email: Email
