from logging import getLogger

from src.utils.db_helper import exec_query

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
    def get(id):
        query = f"SELECT * FROM BAOCAOTHANHTICH WHERE MABAOCAOTHANHTICH = {id}"
        logger.info(f"executing query: {query}")
        try:
            _, achievemet_report = exec_query(query, mode="fetchone")
            if not achievemet_report:
                return "NotFound", None
            return None, AchievementReport.from_json(achievemet_report)

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
    def insert( year, id_achievement_type, achievement_count):
        query = f"INSERT INTO BAOCAOTHANHTICH(NAM, MALOAITHANHTICH, SOLUONGTHANHTICH) VALUES ({year}, {id_achievement_type}, {achievement_count})"
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None
        
