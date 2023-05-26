from logging import getLogger
from typing import Optional
from fastapi import APIRouter, Form

from src.models.relation import Relation
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/relation")
def get_realtion(id: Optional[str] = None, name: Optional[str] = None):

    if id is not None and name is not None:
        return rcode("NotFound")

    error, relation = Relation.get(id, name)
    if error:
        return rcode(error)

    return {**rcode(1000), "relation": relation}


@router.get("/all_realtions")
def get_all_realtions():
    error, realtions = Relation.get_all()

    if error:
        return rcode(error)

    return {**rcode(1000), "realtions": realtions}


@router.post("/relation")
def post_realtion(
    name: str = Form(None),
):
    error, _ = Relation.insert(name)

    if error:
        return rcode(error)

    return rcode(1000)


@router.put("/relation")
def update_relation(
    id: str = Form(None),
    name: str = Form(None),
):
    error, _ = Relation.update(id, name)

    if error:
        return rcode(error)

    return rcode(error)


@router.delete("/relation")
def delete_relation(
    id: str = Form(None),
):
    error, _ = Relation.delete(id)
    if error:
        return rcode(error)

    return rcode(1000)
