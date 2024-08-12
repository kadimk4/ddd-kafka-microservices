from motor.motor_asyncio import AsyncIOMotorClient
from app.domain.entities.user import User
from bson import ObjectId
from typing import Optional

from app.infra.users.converters import to_document

class MongoDBUserRepo:
    def __init__(self, mongodb_client: AsyncIOMotorClient, mongodb_name: str, mongodb_collection: str):
        self.mongodb_client = mongodb_client
        self.mongodb_name = mongodb_name
        self.mongodb_collection = mongodb_collection
        self.database = mongodb_client[mongodb_name]
        self.collection = self.database[mongodb_collection]

    async def add(self, user: User) -> None:
        document = to_document(user)
        await self.collection.insert_one(document)

    async def delete(self, oid: str) -> None:
        document = await self.collection.find_one_and_delete({'_id': oid})
        return document
