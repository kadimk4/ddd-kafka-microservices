import pytest
from punq import Container

from app.logic.punq import _init_container
from app.infra.users.mongodb import MongoDBUserRepo


def init_test_container():
    container: Container = _init_container()
    return container