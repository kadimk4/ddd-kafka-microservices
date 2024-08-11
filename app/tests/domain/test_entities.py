import pytest

from app.domain.entities.user import User

def test_create_User():
    username = 'Aboba'
    email = 'khaydarshin2007@gmail.com'
    user = User(username, email)

    assert user.username == username
    assert user.email == user.email