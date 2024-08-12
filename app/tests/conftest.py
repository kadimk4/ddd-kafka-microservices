from pytest import fixture
from punq import Container
from app.tests.fixtures import init_test_container
from app.infra.users.mongodb import MongoDBUserRepo

@fixture()
def container() -> Container:
    return init_test_container()

@fixture()
def user_repo(container: Container) -> MongoDBUserRepo:
    return container.resolve(MongoDBUserRepo)
