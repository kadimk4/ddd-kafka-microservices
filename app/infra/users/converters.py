from bson import ObjectId
from app.domain.entities.base import BaseEntity
from app.domain.entities.user import User
from app.domain.values.email import Email


def from_document(document: dict) -> User:
    return User(
            username=document['username'],
            email=Email(document['email']),
            oid=document['_id']
        )


def to_document(user: User) -> dict:
    return {
        '_id': user.oid,
        'username': user.username,
        'email': user.email.as_generic_type()
    }
