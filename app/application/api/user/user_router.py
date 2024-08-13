from fastapi import Depends, status
from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from application.api.user.schemas import (
    CreateUpdateUserRequest,
    GetUserRequest,
    UserResponse,
)
from application.api.schemas import BadRequestSchema
from domain.entities.user import User
from domain.exceptions.base import ApplicationException
from domain.values.email import Email
from logic.commands.users import CreateUserCommand, GetUserCommand
from logic.mediator import Mediator
from logic.punq import init_container
from infra.users.mongodb import MongoDBUserRepo

router = APIRouter(tags=["User"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": UserResponse},
        status.HTTP_400_BAD_REQUEST: {"model": BadRequestSchema},
    },
)
async def create_user_route(
    schema: CreateUpdateUserRequest, container=Depends(init_container)
):
    mediator: Mediator = container.resolve(Mediator)

    try:
        user, *_ = await mediator.handle_command(
            CreateUserCommand(username=schema.username, email=schema.email)
        )
    except ApplicationException as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail={"error": err.message}
        )
    return UserResponse.from_entity(user)


@router.get(
    "/{username}",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_201_CREATED: {"model": UserResponse},
        status.HTTP_400_BAD_REQUEST: {"model": BadRequestSchema},
    },
)
async def get_user_route(username: str, container=Depends(init_container)):
    mediator: Mediator = container.resolve(Mediator)
    try:
        user, *_ = await mediator.handle_command(GetUserCommand(username=username))
    except ApplicationException as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail={"error": err.message}
        )
    return UserResponse.from_entity(user)


@router.delete(
    "/{username}",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": UserResponse},
        status.HTTP_400_BAD_REQUEST: {"model": BadRequestSchema},
    },
)
async def delete_user_route(username: str, container=Depends(init_container)):
    repo: MongoDBUserRepo = container.resolve(MongoDBUserRepo)

    try:
        await repo.delete(username)
        return {"status": "successful"}
    except ApplicationException as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail={"error": err.message}
        )
