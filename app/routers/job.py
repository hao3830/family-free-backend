from logging import getLogger
from fastapi import APIRouter, Form
from typing import Optional

from src.models.job import Job
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/job")
def get_job(id: Optional[str] = None, name: Optional[str] = None):
    if id is None and name is None:
        return rcode("NotFound")

    error, job = Job.get(id, name)
    if error:
        return rcode(error)

    return {**rcode(1000), "job": job}


@router.get("/all_jobs")
def get_all_jobs():
    error, jobs = Job.get_all()

    if error:
        return rcode(error)

    return {**rcode(1000), "jobs": jobs}


@router.post("/job")
def post_job(
    name: str = Form(None),
):
    error, _ = Job.insert(name)

    if error:
        return rcode(error)

    return rcode(1000)


@router.put("/job")
def put_job(
    id: str = Form(None),
    name: str = Form(None),
):
    error, _ = Job.update(id, name)

    if error:
        return rcode(error)

    return rcode(1000)


@router.delete("/job")
def delete_job(
    id: str = Form(None),
):
    error, _ = Job.delete(id)
    if error:
        return rcode(error)

    return rcode(1000)