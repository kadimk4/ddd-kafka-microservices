from pydantic import BaseModel
from pydantic import Field
from app.domain.values.email import Email

class CreateUpdateUserRequest(BaseModel):
    username: str = Field(max_length=40, min_length=4, example='michaelapple')
    email: str = Field(example='michaelcoolaple@example.mail')
    
class UpdateUserRequest(BaseModel):
    username: str = Field(max_length=40, min_length=4, example='michaelapple')
    
class UserResponse(BaseModel):
    username: str = Field(max_length=40, min_length=4, example='michaelapple')
    email: str = Field(example='michaelcoolaple@example.mail')