from logging import getLogger
from fastapi import APIRouter, Form
from typing import Optional

from src.models.achievement import Achievement
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/achievement")
def get_achievement(
    id: Optional[str] = None,
    name: Optional[str] = None,
    id_achievement_type: Optional[str] = None,
    date: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
):
    if (
        id is None
        and name is None
        and id_achievement_type is None
        and date is None
        and start_date is None
        and end_date is None
    ):
        return rcode("NotFound")

    error, achievement = Achievement.get(
        id, name, id_achievement_type, date, start_date, end_date
    )
    if error:
        return rcode(error)

    return {**rcode(1000), "achievements": achievement}


@router.get("/all_achievements")
def get_all_achievements():
    error, achievements = Achievement.get_all()

    if error:
        return rcode(error)

    return {**rcode(1000), "achievements": achievements}


@router.post("/achievement")
def post_achievement(
    name: str = Form(None),
    id_achievement_type: str = Form(None),
    date: str = Form(None),
):
    error, _ = Achievement.insert(name, id_achievement_type, date)

    if error:
        return rcode(error)

    return rcode(1000)


@router.put("/achievement")
def update_achievement(
    id: str = Form(None),
    name: str = Form(None),
    id_achievement_type: str = Form(None),
    date: str = Form(None),
):
    error, _ = Achievement.update(id, name, id_achievement_type, date)
    if error:
        return rcode(error)

    return rcode(1000)


@router.delete("/achievement")
def delete_achievement(id: int = Form(None)):
    error, _ = Achievement.delete(id)

    if error:
        return rcode(error)

    return rcode(1000)
