from logging import getLogger

from src.utils.db_helper import exec_query
from src.utils.helper import generate_random_string

logger = getLogger("app")


class Achievement:
    def __init__(self, id, name, id_achievement_type, date,id_member):
        self.id = id
        self.name = name
        self.id_achievement_type = id_achievement_type
        self.date = date
        self.id_member = id_member

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "id_achievement_type": self.id_achievement_type,
            "date": self.date,
            "id_member": slef.id_member
        }

    @staticmethod
    def from_json(_json):
        return Achievement(
            _json["MATHANHTICH"],
            _json["HOVATEN"],
            _json["MALOAITHANHTICH"],
            _json["NGAYPHATSINH"],
            _json["MATHANHVIEN"],
        )

    @staticmethod
    def get(id, name, id_achievement_type, date, start_date, end_date, id_member):
        query = "SELECT * FROM THANHTICH WHERE "
        is_many_condition = False

        if id is not None:
            is_many_condition = True
            query += f"MATHANHTICH = '{id}'"

        if name is not None:
            if is_many_condition:
                query += " AND "
            is_many_condition = True
            query += f"HOVATEN = '{name}'"

        if id_achievement_type is not None:
            if is_many_condition:
                query += " AND "
            is_many_condition = True
            query += f"MALOAITHANHTICH = '{id_achievement_type}'"

        if date is not None:
            if is_many_condition:
                query += " AND "
            is_many_condition = True
            query += f"NGAYPHATSINH = '{date}'"

        if start_date is not None:
            if is_many_condition:
                query += " AND "
            is_many_condition = True
            query += f"NGAYPHATSINH >= '{start_date}'"

        if end_date is not None:
            if is_many_condition:
                query += " AND "
            is_many_condition = True
            query += f"NGAYPHATSINH <= '{end_date}'"
        
        if id_member is not None:
            if is_many_condition:
                query += " AND "
            is_many_condition = True
            query += f"MATHANHVIEN = {id_member}"

        logger.info(f"executing query: {query}")
        try:
            _, achievements = exec_query(query, mode="fetchall")
            return None, [Achievement.from_json(p) for p in achievements]

        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def get_achievement_members_report(start_year, end_year):
        query = f'''
                SELECT LOAITHANHTICH.TENLOAITHANHTICH, COUNT(*) AS COUNT_OCCURRENCES
                FROM THANHTICH
                JOIN LOAITHANHTICH ON THANHTICH.MALOAITHANHTICH = LOAITHANHTICH.MALOAITHANHTICH
                WHERE YEAR(NGAYPHATSINH) BETWEEN {start_year} AND {end_year}
                GROUP BY LOAITHANHTICH.TENLOAITHANHTICH;
                '''
        logger.info(f"executing query: {query}")
        try:
            _, reponse = exec_query(query, mode="fetchall")
            return None, reponse
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None

    @staticmethod
    def get_all():
        query = f"SELECT * FROM THANHTICH"
        logger.info(f"executing query: {query}")
        try:
            _, achievements = exec_query(query, mode="fetchall")
            return None, [Achievement.from_json(p) for p in achievements]
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None

    @staticmethod
    def insert(name, id_achievement_type, date, id_member):
        id = generate_random_string()
        
        query = f"INSERT INTO THANHTICH (MATHANHTICH, HOVATEN, MALOAITHANHTICH, NGAYPHATSINH,MATHANHVIEN) VALUES ('{id}','{name}', '{id_achievement_type}', '{date}','{id_member}')"
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None

    @staticmethod
    def update(id, name, id_achievement_type, date, id_member):
        query = f"UPDATE THANHTICH SET HOVATEN = '{name}', MALOAITHANHTICH = '{id_achievement_type}', NGAYPHATSINH = '{date}', MATHANHVIEN='{id_member}' WHERE MATHANHTICH = '{id}' "
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
        query = f"DELETE FROM THANHTICH WHERE MATHANHTICH = '{id}'"
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"Cannot execute query: {query}")
            logger.error(err, exc_info=True)
            return "SQLExecuteError", None