from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException
from app.domain.values import email


@dataclass
class EmptyEmailException(ApplicationException):
    email: str

    @property
    def message(self):
        return "Email can't be empty"


class ErrorEmailException(ApplicationException):
    email: str

    @property
    def message(self):
        return "Your email must contain '@': {}...".format(email)

class LenEmailException(ApplicationException):
    email: str

    @property
    def message(self):
        return 'Your email is too long/short: {}...'.format(email)