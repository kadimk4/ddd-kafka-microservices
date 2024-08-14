from dataclasses import dataclass

from domain.entities.user import User
from domain.values.email import Email
from infra.exceptions.users import UserAlreadyExistsException, UserNotExistException
from infra.users.converters import from_document
from infra.users.mongodb import MongoDBUserRepo
from logic.commands.base import BaseCommand, CommandHandler


@dataclass(frozen=True)
class CreateUserCommand(BaseCommand):
    username: str
    email: str


@dataclass(frozen=True)
class GetUserQuery(BaseCommand):
    username: str


@dataclass(frozen=True)
class DeleteUserCommand(BaseCommand):
    username: str


@dataclass(frozen=True)
class UpdateUserCommand(BaseCommand):
    oid: str
    username: str
    email: str


@dataclass(frozen=True)
class CreateUserCommandHandler(CommandHandler[CreateUserCommand, User]):
    user_repo: MongoDBUserRepo

    async def handle(self, command: CreateUserCommand) -> User:
        email = Email(command.email)
        user = User(username=command.username, email=email)

        await self.user_repo.add(user)
        return user


@dataclass(frozen=True)
class GetUserQueryHandler(CommandHandler[GetUserQuery, User]):
    user_repo: MongoDBUserRepo

    async def handle(self, command: GetUserQuery) -> User:
        user = await self.user_repo.find_one(command.username)
        return user


@dataclass(frozen=True)
class DeleteUserCommandHandler(CommandHandler[DeleteUserCommand, User]):
    user_repo: MongoDBUserRepo

    async def handle(self, command: DeleteUserCommand) -> dict:
        user = await self.user_repo.delete(command.username)
        return user


@dataclass(frozen=True)
class UpdateUserCommandHandler(CommandHandler[UpdateUserCommand, User]):
    user_repo: MongoDBUserRepo

    async def handle(self, command: UpdateUserCommand) -> dict:
        email = Email(command.email)
        user = User(username=command.username, email=email)

        await self.user_repo.update_one(command.oid, user)
        return user
