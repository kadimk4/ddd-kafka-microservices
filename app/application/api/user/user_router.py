from fastapi import Depends, status
from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from application.api.user.schemas import (
    CreateUpdateUserRequest,
    GetUserRequest,
    UserResponse,
)
from application.api.schemas import BadRequestSchema
from domain.exceptions.base import ApplicationException
from logic.commands.users import (
    CreateUserCommand,
    DeleteUserCommand,
    GetUserQuery,
    UpdateUserCommand,
)
from logic.mediator import Mediator
from logic.punq import init_container


router = APIRouter(tags=["User"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": UserResponse},
        status.HTTP_400_BAD_REQUEST: {"model": BadRequestSchema},
    },
    name="create_user_route",
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
    name="get_user_route",
)
async def get_user_route(username, container=Depends(init_container)):
    mediator: Mediator = container.resolve(Mediator)
    try:
        user, *_ = await mediator.handle_command(GetUserQuery(username=username))
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
    name="delete_user_route",
)
async def delete_user_route(schema: GetUserRequest, container=Depends(init_container)):
    mediator: Mediator = container.resolve(Mediator)

    try:
        user = await mediator.handle_command(
            DeleteUserCommand(username=schema.username)
        )
    except ApplicationException as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail={"error": err.message}
        )
    return user


@router.patch(
    "/{username}",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": UserResponse},
        status.HTTP_400_BAD_REQUEST: {"model": BadRequestSchema},
    },
    name="update_user_route",
)
async def update_user_route(
    oid: str, schema: CreateUpdateUserRequest, container=Depends(init_container)
):
    mediator: Mediator = container.resolve(Mediator)

    try:
        user = await mediator.handle_command(
            UpdateUserCommand(oid=oid, username=schema.username, email=schema.email)
        )
    except ApplicationException as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail={"error": err.message}
        )
    return user
