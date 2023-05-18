from logging import getLogger
from fastapi import APIRouter, Form

from src.models.achievement_type import AchievementType
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/achievement_type")
def get_achievement_type(id: str):
    error, achievement_type = AchievementType.get(id)
    if error:
        return rcode(error)

    return {**rcode(1000), "achievement_type": achievement_type}


@router.get("/all_achievement_types")
def get_all_achievement_types():
    error, achievement_types = AchievementType.get_all()

    if error:
        return rcode(error)

    return {**rcode(1000), "achievement_types": achievement_types}


@router.post("/achievement_type")
def post_achievement_type(
    name: str = Form(None),
):
    error, _ = AchievementType.insert(name)

    if error:
        return rcode(error)

    return rcode(1000)
