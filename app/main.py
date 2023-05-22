import os
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.utils import rlogger
from routers import (
    member,
    achievement,
    achievement_report,
    achievement_type,
    job,
    dead_location,
    end,
    home_town,
    reason,
    relation,
    report,
)

app = FastAPI()

origins = [
    "*"
]

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LOG_PATH = "logs"
os.makedirs(LOG_PATH, exist_ok=True)

# create logger
log_formatter = logging.Formatter(
    "%(asctime)s %(levelname)s" " %(funcName)s(%(lineno)d) %(message)s"
)
log_handler = rlogger.BiggerRotatingFileHandler(
    "ali",
    LOG_PATH,
    mode="a",
    maxBytes=2 * 1024 * 1024,
    backupCount=200,
    encoding=None,
    delay=0,
)
log_handler.setFormatter(log_formatter)
log_handler.setLevel(logging.INFO)

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

logger.info("INIT LOGGER SUCCESSED")

#  member, achievement_report, achievement_type, job, dead_location, end, home_town, reason, relation, report

app.include_router(member.router)
app.include_router(achievement.router)
app.include_router(achievement_report.router)
app.include_router(achievement_type.router)
app.include_router(job.router)
app.include_router(dead_location.router)
app.include_router(end.router)
app.include_router(home_town.router)
app.include_router(reason.router)
app.include_router(relation.router)
app.include_router(report.router)


@app.get("/")
def healthy_check():
    return "OK"
