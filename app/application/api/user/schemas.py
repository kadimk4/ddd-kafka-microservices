from pydantic import BaseModel
from pydantic import Field
from domain.entities.user import User


class CreateUpdateUserRequest(BaseModel):
    username: str = Field(max_length=40, min_length=4, example="michaelapple")
    email: str = Field(example="michaelcoolaple@example.mail")


class GetUserRequest(BaseModel):
    username: str = Field(max_length=40, min_length=4, example="michaelapple")


class UserResponse(BaseModel):
    oid: str = Field(example="420489a4-a9cf-43d2-abc0-0d989cb4b28f")
    username: str = Field(max_length=40, min_length=4, example="michaelapple")
    email: str = Field(example="michaelcoolaple@example.mail")

    @classmethod
    def from_entity(cls, user: User) -> "UserResponse":
        return UserResponse(
            oid=user.oid, username=user.username, email=user.email.as_generic_type()
        )
