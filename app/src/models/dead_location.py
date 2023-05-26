from logging import getLogger

from src.utils.db_helper import exec_query

logger = getLogger("app")

class DeadLocation:
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
        return DeadLocation(
            _json["MADIADIEMMAITANG"],
            _json["TENDIADIEMMAITANG"],
        )
    
    @staticmethod  
    def get(id, name):
        query = f"SELECT * FROM DIADIEMMAITANG WHERE "
        if id is not None:
            query += f"MADIADIEMMAITANG = {id}"

        if name is not None:
            if id is not None:
                query += " AND "
            query += f"TENDIADIEMMAITANG = '{name}'"

        logger.info(f"executing query: {query}")
        try:
            
            _, dead_locations = exec_query(query, mode="fetchall")
            return None, [DeadLocation.from_json(p) for p in dead_locations]

        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def get_all():
        query = f"SELECT * FROM DIADIEMMAITANG"
        logger.info(f"executing query: {query}")
        try:
            _, dead_locations = exec_query(query, mode="fetchall")
            return None, [DeadLocation.from_json(p) for p in dead_locations]
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None
    
    @staticmethod
    def insert(name):
        query = f'Insert into DIADIEMMAITANG (TENDIADIEMMAITANG) values ("{name}")'
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
        query = f'Update DIADIEMMAITANG set TENDIADIEMMAITANG = "{name}" where MADIADIEMMAITANG = {id}'
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
        query = f"Delete from DIADIEMMAITANG where MADIADIEMMAITANG = {id}"
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None