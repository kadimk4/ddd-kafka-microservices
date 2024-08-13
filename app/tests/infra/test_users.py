import pytest
from faker import Faker
from domain.entities.user import User
from infra.users.mongodb import MongoDBUserRepo
from domain.values.email import Email

faker = Faker()


@pytest.mark.asyncio
async def test_crud_user_success(user_repo: MongoDBUserRepo):
    username = faker.user_name()
    email = faker.email()
    user = User(username=username, email=Email(email))
    await user_repo.add(user)

    user_ = await user_repo.find_one(username=username)
    assert user_ is not None
    assert user_['email'] == email
    assert user_['username'] == username

    username_ = faker.user_name()
    user.username = username_
    await user_repo.update_one(user_['oid'], user)
    updated_user = await user_repo.find_one(username_)
    assert updated_user['username'] != username
    assert updated_user['username'] == username_

    deleted = await user_repo.delete(updated_user['username'])
    
    assert deleted is None


