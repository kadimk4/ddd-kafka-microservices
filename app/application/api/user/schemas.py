from pydantic import BaseModel
from pydantic import Field
from domain.entities.user import User


class CreateUpdateUserRequest(BaseModel):
    username: str = Field(max_length=40, min_length=4, example="michaelapple")
    email: str = Field(example="michaelcoolaple@example.mail")


class GetUserRequest(BaseModel):
    username: str = Field(max_length=40, min_length=4, example="michaelapple")


class UserResponse(BaseModel):
    username: str = Field(max_length=40, min_length=4, example="michaelapple")
    email: str = Field(example="michaelcoolaple@example.mail")

    @classmethod
    def from_entity(cls, user: User) -> "UserResponse":
        return UserResponse(username=user.username, email=user.email.as_generic_type())
