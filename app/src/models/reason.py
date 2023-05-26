# CREATE TABLE IF NOT EXISTS `NGUYENNHAN` (
#     MANGUYENNHAN INT NOT NULL AUTO_INCREMENT,
#     TENNGUYENNHAN VARCHAR(50) NOT NULL,

#     PRIMARY KEY(MANGUYENNHAN)
# )

from logging import getLogger

from src.utils.db_helper import exec_query
from src.utils.helper import generate_random_string

logger = getLogger("app")

class Reason:
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
        return Reason(
            _json["MANGUYENNHAN"],
            _json["TENNGUYENNHAN"],
        )
    
    @staticmethod  
    def get(id, name):
        query = f"SELECT * FROM NGUYENNHAN WHERE "
        if id is not None:
            query += f"MANGUYENNHAN = {id}"
        
        if name is not None:
            if id is not None:
                query += " AND "
            query += f"TENNGUYENNHAN = '{name}'"

        logger.info(f"executing query: {query}")
        try:
            _, reasons = exec_query(query, mode="fetchall")
            return None, [Reason.from_json(p) for p in reasons]
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
        id = generate_random_string()
        query = f'Insert into NGUYENNHAN (MANGUYENNHAN,TENNGUYENNHAN) values ("{id}","{name}")'
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
        query = f"update NGUYENNHAN set TENNGUYENNHAN = '{name}' where MANGUYENNHAN = {id}"
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
        query = f"delete from NGUYENNHAN where MANGUYENNHAN = {id}"
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None