# CREATE TABLE IF NOT EXISTS `NGUYENNHAN` (
#     MANGUYENNHAN INT NOT NULL AUTO_INCREMENT,
#     TENNGUYENNHAN VARCHAR(50) NOT NULL,

#     PRIMARY KEY(MANGUYENNHAN)
# )

from logging import getLogger

from src.utils.db_helper import exec_query

logger = getLogger("app")

class Reason:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def json(self):
        return {
            "MANGUYENNHAN": self.id,
            "TENNGUYENNHAN": self.name,
        }
    
    @staticmethod
    def from_json(_json):
        return Reason(
            _json["id"],
            _json["name"],
        )
    
    @staticmethod  
    def get(id):
        query = f"SELECT * FROM NGUYENNHAN WHERE MANGUYENNHAN = {id}"
        logger.info(f"executing query: {query}")
        try:
            _, reason = exec_query(query, mode="fetchone")
            if not reason:
                return "NotFound", None
            return None, Reason.from_json(reason)

        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def get_all():
        query = f"SELECT * FROM NGUYENNHAN"
        logger.info(f"executing query: {query}")
        try:
            _, reasons = exec_query(query, mode="fetchall")
            return None, [Reason.from_json(p) for p in reasons]
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None
    
    @staticmethod
    def insert(name):
        query = f'Insert into NGUYENNHAN (TENNGUYENNHAN) values ("{name}")'
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None