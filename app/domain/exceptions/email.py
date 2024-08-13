from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class EmptyEmailException(ApplicationException):
    @property
    def message(self):
        return "Email can't be empty"


@dataclass(eq=False)
class ErrorEmailException(ApplicationException):
    email: str

    @property
    def message(self):
        return "Your email must contain '@': {}...".format(self.email)


@dataclass(eq=False)
class LenEmailException(ApplicationException):
    email: str

    @property
    def message(self):
        return "Your email is too long/short: {}...".format(self.email)
