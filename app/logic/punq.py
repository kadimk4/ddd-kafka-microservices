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
    container.register(CreateUserCommandHandler)
    container.register(GetUserQueryHandler)
    container.register(DeleteUserCommandHandler)
    container.register(UpdateUserCommandHandler)
    container.register(Config, instance=Config(), scope=Scope.singleton)

    def init_mediator():
        mediator = Mediator()
        mediator.register_command(
            CreateUserCommand, [container.resolve(CreateUserCommandHandler)]
        )
        mediator.register_command(
            GetUserQuery, [container.resolve(GetUserQueryHandler)]
        )
        mediator.register_command(
            DeleteUserCommand, [container.resolve(DeleteUserCommandHandler)]
        )
        mediator.register_command(
            UpdateUserCommand, [container.resolve(UpdateUserCommandHandler)]
        )
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
