from dataclasses import dataclass
from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class UserAlreadyExistsException(ApplicationException):
    @property
    def message(self):
        return "User already exists, try again"


@dataclass(eq=False)
class UserNotExistException(ApplicationException):
    @property
    def message(self):
        return "User not exists, try again"
