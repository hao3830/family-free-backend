import io
import pandas as pd

from logging import getLogger
from typing import Optional
from fastapi import APIRouter, Form
from fastapi.responses import StreamingResponse

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
    generation: Optional[int] = None,
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
        and id_old_member is None
        and create_at is None
        and generation is None
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
        generation
    )
    if error:
        return rcode(error)

    return {**rcode(1000), "members": member}


@router.get('/increase_and_decrease_members')
def get_increase_and_decrease_members(start_year: int, end_year:int):
    error, rows = Member.increase_and_decrease_member(start_year,end_year)
    
    if error:
        return rcode(error)
    
    return {**rcode(1000), "result": rows}

@router.get('/increase_and_decrease_members_csv')
def get_csv(start_year: int, end_year:int):
    error, rows = Member.increase_and_decrease_member(start_year,end_year)
    if error:
        return rcode(error)
    stream = io.StringIO()

    result = {"NO.": [],"Year": [], "Births": [], "Marriages": [], "Deaths": []}
    for idx, row in enumerate(rows):
        result["NO."] = idx
        result['Year'].append(row['Year'])
        result['Births'].append(row['Births'])
        result['Marriages'].append(row['Marriages'])
        result['Deaths'].append(row['Deaths'])
    stream = io.StringIO()
    df = pd.DataFrame(data=result)
    df.to_csv(stream, index = False)
    response = StreamingResponse(iter([stream.getvalue()]),
                                 media_type="text/csv"
                                )
    response.headers["Content-Disposition"] = "attachment; filename=report.csv"
    return response



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
    id_relation: Optional[str] = Form(None),
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