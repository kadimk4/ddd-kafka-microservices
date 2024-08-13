from dataclasses import dataclass

from logic.exceptions.base import LogicException


@dataclass(eq=False)
class CommandHandlerNotExistsException(LogicException):
    command_type: str

    @property
    def message(self):
        return f"Указанный обработчик не существует {self.command_type}"


@dataclass(eq=False)
class EventHandlerNotExistsException(LogicException):
    event_type: str

    @property
    def message(self):
        return f"Указанный обработчик не существует {self.event_type}"
