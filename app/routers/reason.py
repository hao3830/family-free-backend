from logging import getLogger
from fastapi import APIRouter, Form
from typing import Optional

from src.models.reason import Reason
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/reason")
def get_reason(id: Optional[str] = None, name: Optional[str] = None):
    if id is None and name is None:
        return rcode("NotFound")
    
    error, reason = Reason.get(id, name)
    if error:
        return rcode(error)

    return {**rcode(1000), "reasons": reason}


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

@router.put("/reason")
def update_reason(
    id: str = Form(None),
    name: str = Form(None),
):
    error, _ = Reason.update(id, name)
    if error:
        return rcode(error)
    
    return rcode(1000)

@router.delete("/reason")
def delete_reason(
    id: str = Form(None),
):
    error, _ = Reason.delete(id)
    if error:
        return rcode(error)
    
    return rcode(1000)