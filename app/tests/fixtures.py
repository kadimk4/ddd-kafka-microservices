import pytest
from punq import Container
from logic.punq import _init_container


def init_test_container():
    container: Container = _init_container()
    return container