from logging import getLogger
from typing import Optional
from fastapi import APIRouter, Form

from src.models.member import Member
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/member")
def get_member(
    id: Optional[str] = None,
    name: Optional[str] = None,
    sex: Optional[int] = None,
    birthday: Optional[str] = None,
    address: Optional[str] = None,
    id_relation: Optional[str] = None,
    id_job: Optional[str] = None,
    id_home_town: Optional[str] = None,
    id_old_member: Optional[str] = None,
    create_at: Optional[str] = None,
):
    if (
        id is None
        and name is None
        and sex is None
        and birthday is None
        and address is None
        and id_relation is None
        and id_job is None
        and id_home_town is None
        and id_old_member
        and create_at is None
    ):
        return rcode("NotFound")

    error, member = Member.get(
        id,
        name,
        sex,
        birthday,
        address,
        id_relation,
        id_job,
        id_home_town,
        id_old_member,
        create_at,
    )
    if error:
        return rcode(error)

    return {**rcode(1000), "members": member}


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
    id_relation: str = Form(None),
    id_job: str = Form(None),
    id_home_town: str = Form(None),
    id_old_member: Optional[str] = Form(None),
    create_at: str = Form(None),
):
    error, _ = Member.insert(
        name,
        sex,
        birthday,
        address,
        id_relation,
        id_job,
        id_home_town,
        id_old_member,
        create_at,
    )

    if error:
        return rcode(error)

    return rcode(1000)

@router.put("/member")
def update_member(
    id: str = Form(None),
    name: str = Form(None),
    sex: int = Form(None),
    birthday: str = Form(None),
    address: str = Form(None),
    id_relation: str = Form(None),
    id_job: str = Form(None),
    id_home_town: str = Form(None),
    id_old_member: Optional[str] = Form(None),
    create_at: str = Form(None),
):
    error, _ = Member.update(        id,
        name,
        sex,
        birthday,
        address,
        id_relation,
        id_job,
        id_home_town,
        id_old_member,
        create_at,)
    
    if error:
        return rcode(error)
    
    return rcode(1000)

@router.delete("/member")
def delete_member(id: str = Form(None)):
    error, _ = Member.delete(id)
    if error:
        return rcode(error)

    return rcode(1000)