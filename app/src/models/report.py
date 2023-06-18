from logging import getLogger

from src.utils.db_helper import exec_query
from src.utils.helper import generate_random_string

logger = getLogger("app")


class Report:
    def __init__(self, id, nam, soluongsinh, soluonkethon, soluongmat):
        self.id = id
        self.nam = nam
        self.soluongsinh = soluongsinh
        self.soluonkethon = soluonkethon
        self.soluongmat = soluongmat

    def json(self):
        return {
            "id ": self.id,
            "nam ": self.nam,
            "soluongsinh ": self.soluongsinh,
            "soluonkethon ": self.soluonkethon,
            "soluongmat ": self.soluongmat,
        }

    @staticmethod
    def from_json(_json):
        return Report(
            _json["MABAOCAOTANGGIAM"],
            _json["NAM"],
            _json["SOLUONGSINH"],
            _json["SOLUONKETHON"],
            _json["SOLUONGMAT"],
        )

    @staticmethod
    def get(id, nam, soluongsinh, soluonkethon, soluongmat, nam_bat_dau, nam_ket_thuc):
        query = f"SELECT * FROM BAOCAOTANGGIAM WHERE "
        is_multi_condition = False
        if id is not None:
            query += f"MABAOCAOTANGGIAM = '{id}'"
            is_multi_condition = True
        
        if nam is not None:
            if is_multi_condition:
                query += " AND "
            query += f"NAM = {nam}"
        
        if soluongsinh is not None:
            if is_multi_condition:
                query += " AND "
            query += f"SOLUONGSINH = {soluongsinh}"
        
        if soluonkethon is not None:
            if is_multi_condition:
                query += " AND "
            query += f"SOLUONKETHON = {soluonkethon}"
        
        if soluongmat is not None:
            if is_multi_condition:
                query += " AND "
            query += f"SOLUONGMAT = {soluongmat}"
        
        if nam_bat_dau is not None:
            if is_multi_condition:
                query += " AND "
            query += f"NAM >= {nam_bat_dau}"
        
        if nam_ket_thuc is not None:
            if is_multi_condition:
                query += " AND "
            query += f"NAM <= {nam_ket_thuc}"

        logger.info(f"executing query: {query}")
        try:
            _, reports = exec_query(query, mode="fetchall")
            if not reports:
                return "NotFound", None
            return None, [Report.from_json(report) for report in reports]
        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def get_all():
        query = f"SELECT * FROM BAOCAOTANGGIAM"
        logger.info(f"executing query: {query}")

        try:
            _, reports = exec_query(query, mode="fetchall")
            if not reports:
                return "NotFound", None
            return None, [Report.from_json(report) for report in reports]
        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def insert(year, number_of_births, number_of_marriages, number_of_deaths):
        id = generate_random_string()
        query = f'INSERT INTO BAOCAOTANGGIAM(NAM, SOLUONGSINH, SOLUONKETHON, SOLUONGMAT) VALUES(,"{year}", "{number_of_births}", "{number_of_marriages}", "{number_of_deaths}")'
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def update(id, year, number_of_births, number_of_marriages, number_of_deaths):
        query = f'UPDATE BAOCAOTANGGIAM SET NAM="{year}", SOLUONGSINH="{number_of_births}", SOLUONKETHON="{number_of_marriages}", SOLUONGMAT="{number_of_deaths}" WHERE MABAOCAOTANGGIAM="{id}"'
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None
    
    @staticmethod
    def delete(id):
        query = f'DELETE FROM BAOCAOTANGGIAM WHERE MABAOCAOTANGGIAM="{id}"'
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None