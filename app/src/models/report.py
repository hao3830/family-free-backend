from logging import getLogger

from src.utils.db_helper import exec_query

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
    def get(id):
        query = f"SELECT * FROM BAOCAOTANGGIAM WHERE MABAOCAOTANGGIAM = {id}"
        logger.info(f"executing query: {query}")
        try:
            _, report = exec_query(query, mode="fetchone")
            if not report:
                return "NotFound", None
            return None, Report.from_json(report)
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
        query = f'INSERT INTO BAOCAOTANGGIAM(NAM, SOLUONGSINH, SOLUONKETHON, SOLUONGMAT) VALUES("{year}", "{number_of_births}", "{number_of_marriages}", "{number_of_deaths}")'
        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None
