# CREATE TABLE IF NOT EXISTS `LOAITHANHTICH` (
#     MALOAITHANHTICH INT NOT NULL AUTO_INCREMENT,
#     TENLOAITHANHTICH VARCHAR(50) NOT NULL,

#     PRIMARY KEY(MALOAITHANHTICH)
# )

from logging import getLogger

from src.utils.db_helper import exec_query

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
    def get(id):
        query = f"SELECT * FROM LOAITHANHTICH WHERE MALOAITHANHTICH = {id}"
        logger.info(f"executing query: {query}")
        try:
            _, achievement_type = exec_query(query, mode="fetchone")
            if not achievement_type:
                return "NotFound", None
            return None, AchievementType.from_json(achievement_type)

        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def get_all():
        query = f"SELECT * FROM LOAITHANHTICH"
        try:
            _, achievements_type = exec_query(query, mode="fetchall")
            return None, [AchievementType.from_json(p) for p in achievements_type]
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None
    
    @staticmethod
    def insert():
        pass