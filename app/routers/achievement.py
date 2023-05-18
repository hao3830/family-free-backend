from logging import getLogger
from fastapi import APIRouter, Form

from src.models.achievement import Achievement
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/achievement")
def get_achievement(id: str):
    error, achievement = Achievement.get(id)
    if error:
        return rcode(error)

    return {**rcode(1000), "achievement": achievement}


@router.get("/all_achievements")
def get_all_achievements():
    error, achievements = Achievement.get_all()

    if error:
        return rcode(error)

    return {**rcode(1000), "achievements": achievements}


@router.post("/achievement")
def post_achievement(
    name: str = Form(None),
    id_achievement_type: int = Form(None),
    date: str = Form(None),
):
    error, _ = Achievement.insert(name, id_achievement_type, date)

    if error:
        return rcode(error)

    return rcode(1000)
