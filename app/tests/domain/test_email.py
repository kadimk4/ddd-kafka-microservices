import pytest
from faker import Faker

from domain.exceptions.email import EmptyEmailException, ErrorEmailException, LenEmailException
from domain.values.email import Email

faker = Faker()

def test_create_email_success():
    email_str = faker.email()
    email = Email(email_str)

    assert email.as_generic_type() == email_str

def test_create_email_len_fail():
    with pytest.raises(LenEmailException):
        email_str = 'a'*50+faker.email()
        email = Email(email_str)

def test_create_email_empty_fail():
    with pytest.raises(EmptyEmailException):
        email_str = ''
        email = Email(email_str)

def test_create_strange_email_fail():
    with pytest.raises(ErrorEmailException):
        email_str = faker.name_male()
        email = Email(email_str)
