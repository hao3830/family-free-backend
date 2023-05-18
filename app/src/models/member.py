from logging import getLogger

from src.utils.db_helper import exec_query

logger = getLogger("app")


class Member:
    def __init__(
        self,
        id,
        name,
        sex,
        birthday,
        address,
        id_relation,
        id_job,
        id_home_town,
        id_old_member,
    ):
        self.id = id
        self.name = name
        self.sex = sex
        self.birthday = birthday
        self.address = address
        self.address = address
        self.id_relation = id_relation
        self.id_job = id_job
        self.id_home_town = id_home_town
        self.id_old_member = id_old_member

    def json(self):
        return {
            "id ": self.id,
            "name ": self.name,
            "sex ": self.sex,
            "birthday ": self.birthday,
            "address ": self.address,
            "address ": self.address,
            "id_relation ": self.id_relation,
            "id_job ": self.id_job,
            "id_home_town ": self.id_home_town,
            "id_old_member ": self.id_old_member,
        }

    @staticmethod
    def from_json(_json):
        return Member(
            _json["id"],
            _json["name"],
            _json["sex"],
            _json["birthday"],
            _json["address"],
            _json["id_relation"],
            _json["id_job"],
            _json["id_home_town"],
            _json["id_old_member"],
        )

    @staticmethod
    def get(id):
        query = f"SELECT * FROM THANHVIEN WHERE MATHANHVIEN = {id}"
        logger.info(f"executing query: {query}")
        try:
            _, member = exec_query(query, mode="fetchone")
            if not member:
                return "NotFound", None
            return None, Member.from_json(member)

        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def get_all():
        query = f"SELECT * FROM THANHVIEN"
        logger.info(f"executing query: {query}")
        try:
            _, members = exec_query(query, mode='fetchall')
            if not members:
                return "NotFound", None
            return None, [Member.from_json(member) for member in members]
        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def insert(
        name, sex, birthday, address, id_relation, id_job, id_home_town, id_old_member
    ):
        query = f'INSERT INTO THANHVIEN (HOVATEN, GIOITINH, NGAYGIOSINH, MAQUEQUAN, MANGHENGHIEP, DIACHI, MATHANHVIENCU, MALOAIQUANHE)\
                values ("{name}","{sex}","{birthday}","{id_home_town}","{id_job}","{address}","{id_old_member}","{id_relation}")'

        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None
