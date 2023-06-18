import io
import pandas as pd

from logging import getLogger
from fastapi import APIRouter, Form
from typing import Optional
from fastapi.responses import StreamingResponse, FileResponse

from src.models.achievement import Achievement
from src.rcode import rcode


logger = getLogger("app")

router = APIRouter()


@router.get("/achievement")
def get_achievement(
    id: Optional[str] = None,
    name: Optional[str] = None,
    id_achievement_type: Optional[str] = None,
    date: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    id_member: Optional[str] = None
):
    if (
        id is None
        and name is None
        and id_achievement_type is None
        and date is None
        and start_date is None
        and end_date is None
        and id_member is None
    ):
        return rcode("NotFound")

    error, achievement = Achievement.get(
        id, name, id_achievement_type, date, start_date, end_date, id_member
    )
    if error:
        return rcode(error)

    return {**rcode(1000), "achievements": achievement}

@router.get("/achievement_members_report")
def get_achievement_members_report(start_year: Optional[int] = None, end_year: Optional[int] = None):

    if (start_year is None or end_year is None):
        return rcode("NotFound")

    error, achievement_members_report = Achievement.get_achievement_members_report(start_year,end_year)
    if error:
        return rcode(error)
    
    return {**rcode(1000), "result": achievement_members_report} 

@router.get("/achievement_members_report_csv")
def get_achievement_members_report_csv(start_year: Optional[int] = None, end_year: Optional[int] = None):

    if (start_year is None or end_year is None):
        return rcode("NotFound")

    error, achievement_members_report = Achievement.get_achievement_members_report(start_year,end_year)
    if error:
        return rcode(error)
    
    stream = io.StringIO()

    result = {"No.": [],"Type Achievement": [], "Count": []}
    for idx,row in enumerate(achievement_members_report):
        result['No.'].append(idx)
        result['Type Achievement'].append(row['TENLOAITHANHTICH'])
        result['Count'].append(row['COUNT_OCCURRENCES'])
    # stream = io.StringIO()
    file_path = 'data.xlsx'
    df = pd.DataFrame(data=result)
    df.to_excel(file_path,
              index=False)  

    return FileResponse(file_path, filename=f'{start_year}_{end_year}.xlsx')



@router.get("/all_achievements")
def get_all_achievements():
    error, achievements = Achievement.get_all()

    if error:
        return rcode(error)

    return {**rcode(1000), "achievements": achievements}


@router.post("/achievement")
def post_achievement(
    name: str = Form(None),
    id_achievement_type: str = Form(None),
    date: str = Form(None),
    id_member: str = Form(None),
):
    error, _ = Achievement.insert(name, id_achievement_type, date, id_member)

    if error:
        return rcode(error)

    return rcode(1000)


@router.put("/achievement")
def update_achievement(
    id: str = Form(None),
    name: str = Form(None),
    id_achievement_type: str = Form(None),
    date: str = Form(None),
    id_member: str = Form(None), 
):
    error, _ = Achievement.update(id, name, id_achievement_type, date,id_member)
    if error:
        return rcode(error)

    return rcode(1000)


@router.delete("/achievement")
def delete_achievement(id: str = Form(None)):
    error, _ = Achievement.delete(id)

    if error:
        return rcode(error)

    return rcode(1000)
