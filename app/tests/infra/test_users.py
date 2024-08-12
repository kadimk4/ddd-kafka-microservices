import pytest
from faker import Faker
from app.domain.entities.user import User
from app.infra.users.mongodb import MongoDBUserRepo
from app.domain.values.email import Email

faker = Faker()


@pytest.mark.asyncio
async def test_crud_user_success(user_repo: MongoDBUserRepo):
    username = faker.user_name()
    email = faker.email()
    user = User(username=username, email=Email(email))
    await user_repo.add(user)

    found_user = await user_repo.find_one(username=username)
    assert found_user is not None
    assert found_user.email.as_generic_type() == email
    assert found_user.username == username

    new_username = faker.user_name()
    user.username = new_username
    await user_repo.update_one(found_user.oid, user)
    updated_user = await user_repo.find_one(new_username)
    assert updated_user.username != username
    assert updated_user.username == new_username

    deleted_user = await user_repo.delete(found_user.oid)
    assert deleted_user is None


