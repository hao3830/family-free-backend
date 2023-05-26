from logging import getLogger
from fastapi import APIRouter, Form
from typing import Optional

from src.models.report import Report
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/report")
def get_report(
    id: Optional[int] = None,
    nam: Optional[int] = None,
    soluongsinh: Optional[int] = None,
    soluonkethon: Optional[int] = None,
    soluongmat: Optional[int] = None,
    nam_bat_dau: Optional[int] = None,
    nam_ket_thuc: Optional[int] = None,
):
    if (
        id is None
        and nam is None
        and soluongsinh is None
        and soluonkethon is None
        and soluongmat is None
        and nam_bat_dau is None
        and nam_ket_thuc is None
    ):
        return rcode("NotFound")

    error, report = Report.get(
        id, nam, soluongsinh, soluonkethon, soluongmat, nam_bat_dau, nam_ket_thuc
    )
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
    error, _ = Report.insert(
        year, number_of_births, number_of_marriages, number_of_deaths
    )

    if error:
        return rcode(error)

    return rcode(1000)

@router.put("/report")
def put_report(
    id: int = Form(None),
    year: int = Form(None),
    number_of_births: int = Form(None),
    number_of_marriages: int = Form(None),
    number_of_deaths: int = Form(None),
):
    error, _ = Report.update(
        id, year, number_of_births, number_of_marriages, number_of_deaths)
    
    if error:
        return rcode(error)
    
    return rcode(1000)

@router.delete("/report")
def delete_report(
    id: int = Form(None),):

    error, _ = Report.delete(id)

    if error:
        return rcode(error)
    
    return rcode(1000)