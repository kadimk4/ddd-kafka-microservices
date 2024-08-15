from functools import lru_cache

from motor.motor_asyncio import AsyncIOMotorClient
from punq import Container, Scope

from infra.users.mongodb import MongoDBUserRepo
from logic.commands.users import (
    CreateUserCommand,
    CreateUserCommandHandler,
    DeleteUserCommand,
    DeleteUserCommandHandler,
    GetUserQuery,
    GetUserQueryHandler,
    UpdateUserCommand,
    UpdateUserCommandHandler,
)
from logic.mediator import Mediator
from settings import Config


@lru_cache(1)
def init_container():
    return _init_container()


def _init_container() -> Container:
    container = Container()
    command_handlers = [
        (CreateUserCommand, CreateUserCommandHandler),
        (GetUserQuery, GetUserQueryHandler),
        (DeleteUserCommand, DeleteUserCommandHandler),
        (UpdateUserCommand, UpdateUserCommandHandler),
    ]

    for command, handler in command_handlers:
        container.register(handler)

    container.register(Config, instance=Config(), scope=Scope.singleton)

    def init_mediator():
        mediator = Mediator()
        for command, handler in command_handlers:
            mediator.register_command(command, [container.resolve(handler)])
        return mediator

    def init_mongodb_user_repo():
        config: Config = container.resolve(Config)
        client = AsyncIOMotorClient(config.mongodb_connection_uri)
        return MongoDBUserRepo(
            mongodb_client=client,
            mongodb_name=config.mongodb_user_db,
            mongodb_collection=config.mongodb_user_collection,
        )

    container.register(
        MongoDBUserRepo, factory=init_mongodb_user_repo, scope=Scope.singleton
    )
    container.register(Mediator, factory=init_mediator)

    return container
