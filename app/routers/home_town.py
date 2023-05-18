from logging import getLogger
from fastapi import APIRouter, Form

from src.models.home_town import HomeTown
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/home_town")
def get_home_town(id: str):
    error, home_town = HomeTown.get(id)
    if error:
        return rcode(error)

    return {**rcode(1000), "home_town": home_town}


@router.get("/all_home_towns")
def get_all_home_towns():
    error, home_towns = HomeTown.get_all()

    if error:
        return rcode(error)

    return {**rcode(1000), "home_towns": home_towns}


@router.post("/home_town")
def post_home_town(
    name: str = Form(None),
):
    error, _ = HomeTown.insert(name)

    if error:
        return rcode(error)

    return rcode(1000)
