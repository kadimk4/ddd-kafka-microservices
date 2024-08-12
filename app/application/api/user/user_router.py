from fastapi import Depends, status
from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from app.application.api.user.schemas import CreateUpdateUserRequest, UserResponse
from app.application.api.schemas import BadRequestSchema
from app.domain.entities.user import User
from app.domain.exceptions.base import ApplicationException
from app.domain.values.email import Email
from app.logic.punq import init_container
from app.infra.users.mongodb import MongoDBUserRepo

router = APIRouter(tags=['User'])

@router.post('/', status_code=status.HTTP_201_CREATED, responses={
    status.HTTP_201_CREATED: {'model': UserResponse},
    status.HTTP_400_BAD_REQUEST: {'model': BadRequestSchema}
    })
async def create_user_route(schema: CreateUpdateUserRequest, container=Depends(init_container)):
    repo: MongoDBUserRepo = container.resolve(MongoDBUserRepo)

    try:
        user = User(username=schema.username, email=Email(schema.email))
        await repo.add(user)
    except ApplicationException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': e.message})