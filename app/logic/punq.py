from functools import lru_cache
from punq import Container, Scope
from app.settings import Config
from motor.motor_asyncio import AsyncIOMotorClient
from app.infra.users.mongodb import MongoDBUserRepo

@lru_cache(1)
def init_container():
    return _init_container()

def _init_container() -> Container:
    container = Container()

    container.register(Config, instance=Config(), scope=Scope.singleton)

    def init_mongodb_user_repo():
        config: Config = container.resolve(Config)
        client = AsyncIOMotorClient(config.mongodb_connection_uri)
        return MongoDBUserRepo(
            mongodb_client=client,
            mongodb_name=config.mongodb_user_db,
            mongodb_collection=config.mongodb_user_collection
        )
    
    container.register(MongoDBUserRepo, factory=init_mongodb_user_repo, scope=Scope.singleton)

    return container