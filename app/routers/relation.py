from logging import getLogger
from fastapi import APIRouter, Form

from src.models.relation import Relation
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/relation")
def get_realtion(id: str):
    error, relation = Relation.get(id)
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
