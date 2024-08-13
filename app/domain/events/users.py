from dataclasses import dataclass, field
from uuid import uuid4
from domain.events.base import BaseEvent


@dataclass
class UserCreatedEvent(BaseEvent):
    oid: str = field(default_factory=lambda: str(uuid4()))
    username: str
    email: str


@dataclass
class UserUpdatedEvent(BaseEvent):
    oid: str = field(default_factory=lambda: str(uuid4()))
    username: str
    email: str
