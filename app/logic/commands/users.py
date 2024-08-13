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
class GetUserCommand(BaseCommand):
    username: str


@dataclass(frozen=True)
class CreateUserCommandHandler(CommandHandler[CreateUserCommand, User]):
    user_repo: MongoDBUserRepo

    async def handle(self, command: CreateUserCommand) -> User:
        if await self.user_repo.user_exists(command.username):
            raise UserAlreadyExistsException()

        email = Email(command.email)
        user = User(username=command.username, email=email)

        await self.user_repo.add(user)
        return user


@dataclass(frozen=True)
class GetUserCommandHandler(CommandHandler[GetUserCommand, User]):
    user_repo: MongoDBUserRepo

    async def handle(self, command: GetUserCommand) -> User:
        if not await self.user_repo.user_exists(command.username):
            raise UserNotExistException()

        user = await self.user_repo.find_one(command.username)
        return user
