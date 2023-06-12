from logging import getLogger

from src.utils.db_helper import exec_query
from src.utils.helper import generate_random_string

logger = getLogger("app")


class End:
    def __init__(self, id, name, dead_date, id_reason, id_dead_location):
        self.id = id
        self.name = name
        self.dead_date = dead_date
        self.id_reason = id_reason
        self.id_dead_location = id_dead_location

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "dead_date": self.dead_date,
            "id_reason": self.id_reason,
            "id_dead_location": self.id_dead_location,
        }

    @staticmethod
    def from_json(_json):
        return End(
            _json["MAKETTHUC"],
            _json["HOVATEN"],
            _json["NGAYGIOMAT"],
            _json["MANGUYENNHAN"],
            _json["MADIADIEMMAITANG"],
        )

    @staticmethod
    def get(id, name, dead_date, id_reason, id_dead_location):
        query = f"SELECT * FROM KETTHUC WHERE "
        if id is not None:
            query += f"MAKETTHUC = {id}"

        if name is not None:
            if id is not None:
                query += " AND "
            query += f"HOVATEN = '{name}'"

        if dead_date is not None:
            if id is not None or name is not None:
                query += " AND "
            query += f"NGAYGIOMAT = '{dead_date}'"

        if id_reason is not None:
            if id is not None or name is not None or dead_date is not None:
                query += " AND "
            query += f"MANGUYENNHAN = {id_reason}"

        if id_dead_location is not None:
            if (
                id is not None
                or name is not None
                or dead_date is not None
                or id_reason is not None
            ):
                query += " AND "
            query += f"MADIADIEMMAITANG = {id_dead_location}"

        logger.info(f"executing query: {query}")
        try:
            _, ends = exec_query(query, mode="fetchall")
            return None, [End.from_json(p) for p in ends]
        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def get_all():
        query = f"SELECT * FROM KETTHUC"
        try:
            _, ends = exec_query(query, mode="fetchall")
            return None, [End.from_json(p) for p in ends]
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None

    @staticmethod
    def insert(name, dead_date, id_reason, id_dead_location):
        id = generate_random_string()

        query = f'Insert into KETTHUC (MAKETTHUC, HOVATEN, NGAYGIOMAT, MANGUYENNHAN, MADIADIEMMAITANG) values ("{id}","{name}", "{dead_date}", "{id_reason}", "{id_dead_location}")'
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None

    @staticmethod
    def update(id, name, dead_date, id_reason, id_dead_location):
        query = f"update KETTHUC set HOVATEN = '{name}', NGAYGIOMAT = '{dead_date}', MANGUYENNHAN = '{id_reason}', MADIADIEMMAITANG  = '{id_dead_location}' where MAKETTHUC = '{id}'"
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
        query = f"delete from KETTHUC where MAKETTHUC = '{id}'"
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None