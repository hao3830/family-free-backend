from logging import getLogger
from fastapi import APIRouter, Form

from src.models.job import Job
from src.rcode import rcode

logger = getLogger("app")

router = APIRouter()


@router.get("/job")
def get_job(id: str):
    error, job = Job.get(id)
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
