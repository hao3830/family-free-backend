from logging import getLogger
from fastapi import APIRouter, Form

from src.models.reason import Reason
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/reason")
def get_reason(id: str):
    error, reason = Reason.get(id)
    if error:
        return rcode(error)

    return {**rcode(1000), "reason": reason}


@router.get("/all_reasons")
def get_all_reasons():
    error, reasons = Reason.get_all()

    if error:
        return rcode(error)

    return {**rcode(1000), "reasons": reasons}


@router.post("/reason")
def post_reason(
    name: str = Form(None),
):
    error, _ = Reason.insert(name)

    if error:
        return rcode(error)

    return rcode(1000)
