# generated by fastapi-codegen:
#   filename:  simple.yaml
#   timestamp: 2020-06-19T00:00:00+00:00

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI, Query

from .models import Pets

app = FastAPI()


@app.get('/pets', response_model=Pets)
def list_pets(limit: Optional[int] = None) -> Pets:
    pass


@app.post('/pets', response_model=None)
def create_pets() -> None:
    pass


@app.get('/pets/{pet_id}', response_model=Pets)
def show_pet_by_id(pet_id: str = Query(..., alias='petId')) -> Pets:
    pass
