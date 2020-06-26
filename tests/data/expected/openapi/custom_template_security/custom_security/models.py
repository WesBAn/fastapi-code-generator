# generated by datamodel-codegen:
#   filename:  custom_security.yaml
#   timestamp: 2020-06-19T00:00:00+00:00

from typing import Optional

from pydantic import BaseModel


class Pet(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Error(BaseModel):
    code: int
    message: str


class PetForm(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
