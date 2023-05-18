from logging import getLogger
from fastapi import APIRouter, Form

from src.models.report import Report
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/report")
def get_report(id: str):
    error, report = Report.get(id)
    if error:
        return rcode(error)

    return {**rcode(1000), "report": report}


@router.get("/all_reports")
def get_all_reports():
    error, reports = Report.get_all()

    if error:
        return rcode(error)

    return {**rcode(1000), "reports": reports}


@router.post("/report")
def post_report(
    year: int = Form(None),
    number_of_births: int = Form(None),
    number_of_marriages: int = Form(None),
    number_of_deaths: int = Form(None),
):
    error, _ = Report.insert(year,number_of_births,number_of_marriages,number_of_deaths)

    if error:
        return rcode(error)

    return rcode(1000)
