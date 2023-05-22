from logging import getLogger

from src.utils.db_helper import exec_query

logger = getLogger("app")


class HomeTown:
    def __init__(
        self,
        id,
        name,
    ):
        self.id = id
        self.name = name

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    @staticmethod
    def from_json(_json):
        return HomeTown(
            _json["MAQUEQUAN"],
            _json["TENQUANHE"],
        )

    @staticmethod
    def get(id):
        query = f"SELECT * FROM QUEQUAN WHERE MAQUEQUAN = {id}"
        logger.info(f"executing query: {query}")
        try:
            _, home_town = exec_query(query, mode="fetchone")
            if not home_town:
                return "NotFound", None
            return None, HomeTown.from_json(home_town)

        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def get_all():
        query = f"SELECT * FROM QUEQUAN"
        try:
            _, home_towns = exec_query(query, mode="fetchall")
            return None, [HomeTown.from_json(p) for p in home_towns]
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None

    @staticmethod
    def insert(name):
        query = f'Insert into QUEQUAN (TENQUANHE) values ("{name}")'
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None
