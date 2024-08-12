from bson import ObjectId
from app.domain.entities.base import BaseEntity
from app.domain.entities.user import User
from app.domain.values.email import EmailStr

def from_document(document: dict) -> User:
    return User(document.__dict__)

def to_document(user: User) -> dict:
    return {
        '_id': user.oid,
        'username': user.username,
        'email': user.email.as_generic_type()
    }