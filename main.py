from fastapi import Depends, FastAPI
from app.domain.entities.user import User
from app.domain.values.email import EmailStr
from app.logic.punq import init_container
from app.infra.users.mongodb import MongoDBUserRepo

app = FastAPI()


@app.get("/{username}/{email}")
async def create(username: str, email: str, container=Depends(init_container)):
    repo: MongoDBUserRepo = container.resolve(MongoDBUserRepo)
    email = EmailStr(email)
    user = User(username=username, email=email)
    await repo.add(user)
    return {'created': 'successful'}

@app.get('/{oid}')
async def delete(oid: str, container=Depends(init_container)):
    repo: MongoDBUserRepo = container.resolve(MongoDBUserRepo)
    document = await repo.delete(oid)
    return {'status': 'successful', 'user': document}