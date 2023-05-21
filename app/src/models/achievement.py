from logging import getLogger

from src.utils.db_helper import exec_query

logger = getLogger("app")


class Achievement:
    def __init__(self, id, name, id_achievement_type, date):
        self.id = id
        self.name = name
        self.id_achievement_type = id_achievement_type
        self.date = date

    def json(self):
        return {
            "MATHANHTICH": self.id,
            "HOVATEN": self.name,
            "MALOAITHANHTICH": self.id_achievement_type,
            "NGAYPHATSINH": self.date,
        }

    @staticmethod
    def from_json(_json):
        return Achievement(
            _json["id"], _json["name"], _json["id_achievement_type"], _json["date"]
        )

    @staticmethod
    def get(id):
        query = f"SELECT * FROM THANHTICH WHERE MATHANHTICH = {id}"
        logger.info(f"executing query: {query}")
        try:
            _, achievement = exec_query(query, mode="fetchone")
            if not achievement:
                return "NotFound", None
            return None, Achievement.from_json(achievement)

        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def get_all():
        query = f"SELECT * FROM THANHTICH"
        try:
            _, achievements = exec_query(query, mode="fetchall")
            return None, [Achievement.from_json(p) for p in achievements]
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None
    
    @staticmethod
    def insert(
        name, id_achievement_type, date
    ):
        query = f"INSERT INTO THANHTICH (HOVATEN, MALOAITHANHTICH, NGAYPHATSINH) VALUES ('{name}', {id_achievement_type}, '{date}')"
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None