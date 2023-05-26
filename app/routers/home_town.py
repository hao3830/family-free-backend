from logging import getLogger
from fastapi import APIRouter, Form
from typing import Optional

from src.models.home_town import HomeTown
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/home_town")
def get_home_town(id: Optional[str] = None, name: Optional[str] = None):
    if id is None and name is None:
        return rcode("NotFound")

    error, home_town = HomeTown.get(id, name)
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


@router.put("/home_town")
def update_home_town(
    id: str = Form(None),
    name: str = Form(None),
):
    error, _ = HomeTown.update(id, name)
    if error:
        return rcode(error)

    return rcode(1000)


@router.delete("/home_town")
def delete_home_town(id: str = Form(None)):
    error, _ = HomeTown.delete(id)

    if error:
        return rcode(error)

    return rcode(1000)
