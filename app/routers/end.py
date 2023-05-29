from logging import getLogger
from fastapi import APIRouter, Form
from typing import Optional

from src.models.end import End
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/end")
def get_end(
    id: Optional[str] = None,
    name: Optional[str] = None,
    dead_date: Optional[str] = None,
    id_reason: Optional[str] = None,
    id_dead_location: Optional[str] = None,
):
    if (
        id is None
        and name is None
        and dead_date is None
        and id_reason is None
        and id_dead_location is None
    ):
        return rcode("NotFound")

    error, end = End.get(id, name, dead_date, id_reason, id_dead_location)
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
    id_reason: str = Form(None),
    id_dead_location: str = Form(None),
):
    error, _ = End.insert(name, dead_date, id_reason, id_dead_location)

    if error:
        return rcode(error)

    return rcode(1000)


@router.put("/end")
def update_end(
    id: str = Form(None),
    name: str = Form(None),
    dead_date: str = Form(None),
    id_reason: str = Form(None),
    id_dead_location: str = Form(None),
):
    error, _ = End.update(id, name, dead_date, id_reason, id_dead_location)
    if error:
        return rcode(error)

    return rcode(1000)


@router.delete("/end")
def delete_end(
    id: str = Form(None),
):
    error, _ = End.delete(id)
    if error:
        return rcode(error)

    return rcode(1000)
