import pytest
from faker import Faker

from app.domain.exceptions.email import EmptyEmailException, ErrorEmailException, LenEmailException
from app.domain.values.email import EmailStr

faker = Faker()

def test_create_email_successful():
    email_str = faker.email()
    email = EmailStr(email_str)

    assert email.as_generic_type() == email_str

def test_create_email_len_failed():
    with pytest.raises(LenEmailException):
        email_str = 'a'*50+faker.email()
        email = EmailStr(email_str)

def test_create_email_empty_failed():
    with pytest.raises(EmptyEmailException):
        email_str = ''
        email = EmailStr(email_str)

def test_create_strange_email_failed():
    with pytest.raises(ErrorEmailException):
        email_str = faker.name_male()
        email = EmailStr(email_str)
