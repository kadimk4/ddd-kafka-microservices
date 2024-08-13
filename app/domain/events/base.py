from abc import ABC
from dataclasses import field, dataclass
from uuid import uuid4


@dataclass
class BaseEvent(ABC):
    event_id: str = field(default_factory=lambda: str(uuid4()))
