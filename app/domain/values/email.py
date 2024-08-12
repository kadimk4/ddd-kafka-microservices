from dataclasses import dataclass
from re import match as mt
from app.domain.exceptions.email import EmptyEmailException, ErrorEmailException, LenEmailException
from app.domain.values.base import BaseValueObject 

pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"

@dataclass(frozen=True)
class Email(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyEmailException()

        if mt(pattern, self.value) is None:
            raise ErrorEmailException(self.value)

        if len(self.value) >= 40 or len(self.value) <= 6:
            raise LenEmailException(self.value)

    def as_generic_type(self) -> str:
        return str(self.value)
