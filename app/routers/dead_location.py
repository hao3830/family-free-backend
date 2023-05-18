from logging import getLogger
from fastapi import APIRouter, Form

from src.models.dead_location import DeadLocation
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/dead_location")
def get_dead_location(id: str):
    error, dead_location = DeadLocation.get(id)
    if error:
        return rcode(error)

    return {**rcode(1000), "dead_location": dead_location}


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
