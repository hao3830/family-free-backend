from logging import getLogger
from fastapi import APIRouter, Form
from typing import Optional

from src.models.dead_location import DeadLocation
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/dead_location")
def get_dead_location(id: Optional[int], name: Optional[str]):
    if id is None and name is None:
        return rcode("NotFound")

    error, dead_locations = DeadLocation.get(id, name)
    if error:
        return rcode(error)

    return {**rcode(1000), "dead_locations": dead_locations}


@router.get("/all_dead_locations")
def get_all_dead_locations():
    error, dead_locations = DeadLocation.get_all()

    if error:
        return rcode(error)

    return {**rcode(1000), "dead_locations": dead_locations}


@router.post("/dead_location")
def post_dead_location(
    name: str = Form(None),
):
    error, _ = DeadLocation.insert(name)

    if error:
        return rcode(error)

    return rcode(1000)


@router.put("/dead_location")
def update_dead_location(id: int = Form(None), name: str = Form(None)):
    error, _ = DeadLocation.update(id, name)
    if error:
        return rcode(error)

    return rcode(1000)


@router.delete("/dead_location")
def delete_dead_location(id: int = Form(None)):
    error, _ = DeadLocation.delete(id)
    if error:
        return rcode(error)

    return rcode(1000)
