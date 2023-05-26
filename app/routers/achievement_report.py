from logging import getLogger
from fastapi import APIRouter, Form
from typing import Optional

from src.models.achievement_report import AchievementReport
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/achievement_report")
def get_achievement_report(
    id: Optional[str] = None,
    year: Optional[int] = None,
    id_achievement_type: Optional[int] = None,
    achievement_count: Optional[int] = None,
):
    if (
        id is None
        and year is None
        and id_achievement_type is None
        and achievement_count is None
    ):
        return rcode("NotFound")
    
    error, achievement_report = AchievementReport.get(
        id, year, id_achievement_type, achievement_count
    )
    if error:
        return rcode(error)

    return {**rcode(1000), "achievement_reports": achievement_report}


@router.get("/all_achievement_reports")
def get_all_achievement_reports():
    error, achievement_reports = AchievementReport.get_all()

    if error:
        return rcode(error)

    return {**rcode(1000), "achievement_reports": achievement_reports}


@router.post("/achievement_report")
def post_achievement_report(
    year: int = Form(None),
    id_achievement_type: int = Form(None),
    achievement_count: int = Form(None),
):
    error, _ = AchievementReport.insert(year, id_achievement_type, achievement_count)

    if error:
        return rcode(error)

    return rcode(1000)

@router.put("/achievement_report")
def put_achievement_report(
    id: str = Form(None),
    year: int = Form(None),
    id_achievement_type: int = Form(None),
    achievement_count: int = Form(None),
):
    error, _ = AchievementReport.update(
        id, year, id_achievement_type, achievement_count
    )

    if error:
        return rcode(error)

    return rcode(1000)

@router.delete("/achievement_report")
def delete_achievement_report(id: str = Form(None)):
    error, _ = AchievementReport.delete(id)

    if error:
        return rcode(error)

    return rcode(1000)