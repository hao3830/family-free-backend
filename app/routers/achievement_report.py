from logging import getLogger
from fastapi import APIRouter, Form

from src.models.achievement_report import AchievementReport
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/achievement_report")
def get_achievement_report(id: str):
    error, achievement_report = AchievementReport.get(id)
    if error:
        return rcode(error)

    return {**rcode(1000), "achievement_report": achievement_report}


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
