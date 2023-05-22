from logging import getLogger

from src.utils.db_helper import exec_query

logger = getLogger("app")


class Relation:
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
        return Relation(
            _json["MALOAIQUANHE"],
            _json["TENLOAIQUANHE"],
        )

    @staticmethod
    def get(id):
        query = f"SELECT * FROM QUANHE WHERE MAQUANHE = {id}"
        logger.info(f"executing query: {query}")
        try:
            _, realtion = exec_query(query, mode="fetchone")
            if not realtion:
                return "NotFound", None
            return None, Relation.from_json(realtion)

        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def get_all():
        query = f"SELECT * FROM QUANHE"
        try:
            _, relation = exec_query(query, mode="fetchall")
            return None, [Relation.from_json(p) for p in relation]
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None

    @staticmethod
    def insert(name):
        query = f'Insert into QUANHE (TENLOAIQUANHE) values ("{name}")'
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None
