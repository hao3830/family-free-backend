# CREATE TABLE IF NOT EXISTS `LOAITHANHTICH` (
#     MALOAITHANHTICH INT NOT NULL AUTO_INCREMENT,
#     TENLOAITHANHTICH VARCHAR(50) NOT NULL,

#     PRIMARY KEY(MALOAITHANHTICH)
# )

from logging import getLogger

from src.utils.db_helper import exec_query
from src.utils.helper import generate_random_string

logger = getLogger("app")

class AchievementType:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def json(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @staticmethod
    def from_json(_json):
        return AchievementType(_json["MALOAITHANHTICH"], _json["TENLOAITHANHTICH"])

    @staticmethod
    def get(id, name):
        query = "SELECT * FROM LOAITHANHTICH WHERE "
        if id is not None:
            query += f"MALOAITHANHTICH = '{id}'"
        
        if name is not None:
            if id is not None:
                query += " AND "
            query += f"TENLOAITHANHTICH = '{name}'"

        logger.info(f"executing query: {query}")
        try:
            _, achievements_type = exec_query(query, mode="fetchall")
            return None, [AchievementType.from_json(p) for p in achievements_type]
        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def get_all():
        query = f"SELECT * FROM LOAITHANHTICH"
        logger.info(f"executing query: {query}")

        try:
            _, achievements_type = exec_query(query, mode="fetchall")
            return None, [AchievementType.from_json(p) for p in achievements_type]
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None
    
    @staticmethod
    def insert(name):
        id = generate_random_string()
        query = f'Insert into LOAITHANHTICH ( TENLOAITHANHTICH) values ("{name}")'
        logger.info(f"executing query: {query}")
        
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None
    
    @staticmethod
    def update(id, name):
        query = f'Update LOAITHANHTICH set TENLOAITHANHTICH = "{name}" where MALOAITHANHTICH = "{id}"'
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
        query = f'Delete from LOAITHANHTICH where MALOAITHANHTICH = "{id}"'
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None