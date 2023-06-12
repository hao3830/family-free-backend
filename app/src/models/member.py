from logging import getLogger

from src.utils.db_helper import exec_query
from src.utils.helper import generate_random_string

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
        create_at,
        generation
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
        self.create_at = create_at
        self.generation = generation

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
            "create_at": self.create_at,
            "generation" : self.generation,
        }

    @staticmethod
    def from_json(_json):
        return Member(
            _json["MATHANHVIEN"],
            _json["HOVATEN"],
            _json["GIOITINH"],
            _json["NGAYGIOSINH"],
            _json["DIACHI"],
            _json["MALOAIQUANHE"],
            _json["MANGHENGHIEP"],
            _json["MAQUEQUAN"],
            _json["MATHANHVIENCU"],
            _json["NGAYPHATSINH"],
            _json["THEHE"],
        )

    @staticmethod
    def get(
        id = None,
        name = None,
        sex = None,
        birthday = None,
        address = None,
        id_relation = None,
        id_job = None,
        id_home_town = None,
        id_old_member = None,
        create_at = None,
        generation = None,
    ):
        query = f"SELECT * FROM THANHVIEN WHERE "
        is_multi_condition = False
        if id is not None:
            is_multi_condition = True
            query += f"MATHANHVIEN = '{id}'"

        if name is not None:
            if is_multi_condition:
                query += " AND "
            is_multi_condition = True
            query += f"HOVATEN = '{name}'"

        if sex is not None:
            if is_multi_condition:
                query += " AND "
            is_multi_condition = True
            query += f"GIOITINH = {sex}"

        if birthday is not None:
            if is_multi_condition:
                query += " AND "
            is_multi_condition = True
            query += f"NGAYGIOSINH = '{birthday}'"

        if address is not None:
            if is_multi_condition:
                query += " AND "
            is_multi_condition = True
            query += f"DIACHI = '{address}'"

        if id_relation is not None:
            if is_multi_condition:
                query += " AND "
            query += f"MALOAIQUANHE = '{id_relation}'"

        if id_job is not None:
            if is_multi_condition:
                query += " AND "
            is_multi_condition = True
            query += f"MANGHENGHIEP = '{id_job}'"

        if id_home_town is not None:
            if is_multi_condition:
                query += " AND "
            is_multi_condition = True
            query += f"MAQUEQUAN = '{id_home_town}'"

        if id_old_member is not None:
            if is_multi_condition:
                query += " AND "
            is_multi_condition = True
            query += f" MATHANHVIENCU = '{id_old_member}'"

        if create_at is not None:
            if is_multi_condition:
                query += " AND "
            is_multi_condition = True
            query += f"NGAYPHATSINH = '{create_at}'"
        
        if generation is not None:
            if is_multi_condition:
                query += " AND "
            is_multi_condition = True
            query += f"THEHE = {generation}"

        logger.info(f"executing query: {query}")
        try:
            _, members = exec_query(query, mode="fetchall")
            if not members:
                return "NotFound", None
            return None, [Member.from_json(member) for member in members]

        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def get_all():
        query = f"SELECT * FROM THANHVIEN"
        logger.info(f"executing query: {query}")
        try:
            _, members = exec_query(query, mode="fetchall")
            if not members:
                return "NotFound", None
            return None, [Member.from_json(member) for member in members]
        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def insert(
        name,
        sex,
        birthday,
        address,
        id_relation,
        id_job,
        id_home_town,
        id_old_member,
        create_at,
    ):
        id = generate_random_string()

        if id_old_member is None:
            genration = 0
        else:
            error, old_members = Member.get(id=id_old_member)
            if error is not None:
                return error, None

            genration = old_members[0].generation
        
        if id_relation == '01':
            genration += 1

        query = f'INSERT INTO THANHVIEN (MATHANHVIEN, HOVATEN, GIOITINH, NGAYGIOSINH, MAQUEQUAN, MANGHENGHIEP, DIACHI, MATHANHVIENCU, MALOAIQUANHE, NGAYPHATSINH, THEHE)\
                values ("{id}","{name}","{sex}","{birthday}","{id_home_town}","{id_job}","{address}","{id_old_member}","{id_relation}","{create_at}","{genration}")'

        logger.info(f"executing query: {query}")
        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None

    @staticmethod
    def update(
        id,
        name,
        sex,
        birthday,
        address,
        id_relation,
        id_job,
        id_home_town,
        id_old_member,
        create_at,
    ):
        if id_old_member is None:
            genration = 0
        else:
            error, old_members = Member.get(id=id_old_member)
            if error is not None:
                return error, None

            genration = old_members[0].generation
        
        if id_relation == '01':
            genration += 1

        query = f"update THANHVIEN set HOVATEN = '{name}', GIOITINH = {sex}, \
            NGAYGIOSINH = '{birthday}', MAQUEQUAN = '{id_home_town}', MANGHENGHIEP = '{id_job}',\
            DIACHI = '{address}', MALOAIQUANHE = '{id_relation}', MATHANHVIENCU = '{id_old_member}'\
            NGAYPHATSINH = '{create_at}', THEHE = {genration} where MATHANHVIEN = '{id}'"

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
        query = f"delete from THANHVIEN where MATHANHVIEN = '{id}'"
        logger.info(f"executing query: {query}")

        try:
            exec_query(query)
            return None, None
        except Exception as err:
            logger.error(f"can not execute query: {query}")
            logger.error(err)
            return "SQLExecuteError", None