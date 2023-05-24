from logging import getLogger
from typing import Union
from fastapi import APIRouter, Form

from src.models.member import Member
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/member")
def get_member(id: str):
    error, member = Member.get(id)
    if error:
        return rcode(error)

    return {**rcode(1000), "member": member}


@router.get("/all_members")
def get_all_members():
    error, members = Member.get_all()

    if error:
        return rcode(error)

    return {**rcode(1000), "members": members}


@router.post("/member")
def post_member(
    name: str = Form(None),
    sex: int = Form(None),
    birthday: str = Form(None),
    address: str = Form(None),
    id_relation: int = Form(None),
    id_job: int = Form(None),
    id_home_town: int = Form(None),
    id_old_member: Union[int, None] = Form(None),
):
    error, _ = Member.insert(
        name, sex, birthday, address, id_relation, id_job, id_home_town, id_old_member
    )

    if error:
        return rcode(error)

    return rcode(1000)
