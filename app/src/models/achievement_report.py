from logging import getLogger

from src.utils.db_helper import exec_query
from src.utils.helper import generate_random_string

logger = getLogger("app")


class AchievementReport:
    def __init__(self, id, year, id_achievement_type, achievement_count):
        self.id = id
        self.year = year
        self.id_achievement_type = id_achievement_type
        self.achievement_count = achievement_count

    def json(self):
        return {
            "id": self.id,
            "year": self.year,
            "id_achievement_type": self.id_achievement_type,
            "achievement_count": self.achievement_count,
        }

    @staticmethod
    def from_json(_json):
        return AchievementReport(
            _json["MABAOCAOTHANHTICH"],
            _json["NAM"],
            _json["MALOAITHANHTICH"],
            _json["SOLUONGTHANHTICH"],
        )

    @staticmethod
    def get(id, year, id_achievement_type, achievement_count):
        query = "SELECT * FROM BAOCAOTHANHTICH WHERE "

        if id is not None:
            query += f"MABAOCAOTHANHTICH = {id}"

        if year is not None:
            if id is not None:
                query += " AND "
            query += f"NAM = {year}"

        if id_achievement_type is not None:
            if id is not None or year is not None:
                query += " AND "
            query += f"MALOAITHANHTICH = {id_achievement_type}"

        if achievement_count is not None:
            if id is not None or year is not None or id_achievement_type is not None:
                query += " AND "
            query += f"SOLUONGTHANHTICH = {achievement_count}"

        logger.info(f"executing query: {query}")
        try:
            _, achievement_reports = exec_query(query, mode="fetchall")
            return None, [AchievementReport.from_json(p) for p in achievement_reports]

        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def get_all():
        query = f"SELECT * FROM BAOCAOTHANHTICH"
        try:
            _, achievement_reports = exec_query(query, mode="fetchall")
            return None, [AchievementReport.from_json(p) for p in achievement_reports]
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None

    @staticmethod
    def insert(year, id_achievement_type, achievement_count):
        id = generate_random_string()
        query = f"INSERT INTO BAOCAOTHANHTICH(MABAOCAOTHANHTICH, NAM, MALOAITHANHTICH, SOLUONGTHANHTICH) VALUES ({id},{year}, {id_achievement_type}, {achievement_count})"
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None

    @staticmethod
    def update(id, year, id_achievement_type, achievement_count):
        query = f"UPDATE BAOCAOTHANHTICH SET NAM = {year}, MALOAITHANHTICH = {id_achievement_type}, SOLUONGTHANHTICH = {achievement_count} WHERE MABAOCAOTHANHTICH = {id}"
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None

    @staticmethod
    def delete(id):
        query = f"DELETE FROM BAOCAOTHANHTICH WHERE MABAOCAOTHANHTICH = {id}"
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None