from logging import getLogger

from src.utils.db_helper import exec_query

logger = getLogger("app")

class Job:
    def __ini__(self, id, name):
        self.id = id
        self.name = name
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
        }
    
    @staticmethod
    def from_json(_json):
        return Job(
            _json["id"],
            _json["name"],
        )
    
    @staticmethod  
    def get(id):
        query = f"SELECT * FROM NGHENGHIEP WHERE MANGHENGHIEP = {id}"
        logger.info(f"executing query: {query}")
        try:
            _, job = exec_query(query, mode="fetchone")
            if not job:
                return "NotFound", None
            return None, Job.from_json(job)

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
        query = f'Insert into NGHENGHIEP (TENNGHENGHIEP) values ("{name}")'
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None