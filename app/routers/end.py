from logging import getLogger
from fastapi import APIRouter, Form

from src.models.end import End
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/end")
def get_end(id: str):
    error, end = End.get(id)
    if error:
        return rcode(error)

    return {**rcode(1000), "end": end}


@router.get("/all_ends")
def get_all_ends():
    error, ends = End.get_all()

    if error:
        return rcode(error)

    return {**rcode(1000), "ends": ends}


@router.post("/end")
def post_end(
    name: str = Form(None),
    dead_date: str = Form(None),
    id_reason: int = Form(None),
    id_dead_location: int = Form(None),
):
    error, _ = End.insert(name, dead_date, id_reason, id_dead_location)

    if error:
        return rcode(error)

    return rcode(1000)
