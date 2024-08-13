from motor.motor_asyncio import AsyncIOMotorClient
from domain.entities.user import User

from infra.exceptions.users import UserAlreadyExistsException, UserNotExistException
from infra.users.converters import to_document, from_document


class MongoDBUserRepo:
    def __init__(
        self,
        mongodb_client: AsyncIOMotorClient,
        mongodb_name: str,
        mongodb_collection: str,
    ):
        self.mongodb_client = mongodb_client
        self.mongodb_name = mongodb_name
        self.mongodb_collection = mongodb_collection
        self.database = mongodb_client[mongodb_name]
        self.collection = self.database[mongodb_collection]

    async def user_exists(self, username: str) -> bool:
        user = await self.collection.find_one({"username": username}) is not None
        return user

    async def add(self, user: User) -> dict:
        if not await self.user_exists(user.username):
            document = to_document(user)
            await self.collection.insert_one(document)
            return {
                "oid": user.oid,
                "username": user.username,
                "email": user.email.as_generic_type(),
            }
        raise UserAlreadyExistsException()

    async def find_one(self, username: str) -> dict | None:
        if await self.user_exists(username):
            document = await self.collection.find_one({"username": username})
            user = from_document(document)
            return user
        raise UserNotExistException()

    async def update_one(self, oid: str, user: User) -> None:
        document = to_document(user)
        if await self.collection.find_one({"_id": oid}):
            await self.collection.update_one({"_id": oid}, {"$set": document})
        else:
            raise UserNotExistException()

    async def delete(self, username: str) -> None:
        if await self.user_exists(username):
            await self.collection.find_one_and_delete({"username": username})
        else:
            raise UserNotExistException()
