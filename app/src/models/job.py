from logging import getLogger

from src.utils.db_helper import exec_query
from src.utils.helper import generate_random_string

logger = getLogger("app")


class Job:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    @staticmethod
    def from_json(_json):
        return Job(id=_json["MANGHENGHIEP"], name=_json["TENNGHENGHIEP"])

    @staticmethod
    def get(id, name):
        query = f"SELECT * FROM NGHENGHIEP WHERE "
        if id is not None:
            query += f"MANGHENGHIEP = '{id}'"

        if name is not None:
            if id is not None:
                query += " AND "
            query += f"TENNGHENGHIEP = '{name}'"

        logger.info(f"executing query: {query}")
        try:
            _, jobs = exec_query(query, mode="fetchall")
            return None, [Job.from_json(p) for p in jobs]

        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def get_all():
        query = f"SELECT * FROM NGHENGHIEP"
        logger.info(f"executing query: {query}")
        try:
            _, jobs = exec_query(query, mode="fetchall")
            return None, [Job.from_json(p) for p in jobs]
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None

    @staticmethod
    def insert(name):
        id = generate_random_string()
        
        query = f'Insert into NGHENGHIEP (MANGHENGHIEP,TENNGHENGHIEP) values ("{id}","{name}")'
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None

    @staticmethod
    def update(id,name):
        query = f"update NGHENGHIEP set TENNGHENGHIEP = '{name}' where MANGHENGHIEP = '{id}'"
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None
    
    @staticmethod
    def delete(id):
        query = f"delete from NGHENGHIEP where MANGHENGHIEP = '{id}'"
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None 
        