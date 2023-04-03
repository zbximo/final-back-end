# -*- encoding: utf-8 -*-
# @ModuleName: UserService
# @Author: ximo
# @Time: 2023/3/28 14:54
import json
import time

from sqlalchemy import func

from service.Mysql.db_connector import MysqlConnect
from utils import model_json
from sqlalchemy.orm.session import Session
from service.Mysql.model import *


class UserService:
    def __init__(self, mysql_session):
        self.mysql_session = mysql_session

    # ----------------------------InitSpace Start--------------------------------------------
    def get_all_user(self):
        """
        NodeUserInfo
        :return:
        """
        mysql_session = self.mysql_session()
        return mysql_session.query(TbInfoUser).all()

    def get_all_app_user(self):
        """
        RelationAppUser
        :return: List<TbInfoAppUser>
        """
        mysql_session: Session = self.mysql_session()
        result = mysql_session.query(TbInfoAppUser).all()
        return result

    def get_all_app_groups(self):
        mysql_session: Session = self.mysql_session()
        result = mysql_session.query(TbInfoGroup, TbInfoApp).join(TbInfoApp, isouter=True).all()
        return result

    def get_all_app_name_user(self):
        """
        提供NodeAppUserInfo
        :return: List<(TbInfoAppUser, TbInfoApp)>
        """
        mysql_session: Session = self.mysql_session()
        # mysql = "select * from "
        # print(mysql_session.query(TbInfoAppUser, TbInfoApp).join(TbInfoApp, isouter=True))
        result = mysql_session.query(TbInfoAppUser, TbInfoApp).join(TbInfoApp, isouter=True).all()
        return result

    def get_all_group_user(self):
        """
        List<TbInfoGroupUser>
        :return:
        """
        # 查询出group user
        mysql_session: Session = self.mysql_session()
        result = mysql_session.query(TbInfoGroupUser).all()
        # 查询记录

        return result

    def get_all_user_telephones(self):
        mysql_session: Session = self.mysql_session()
        result = mysql_session.query(TbInfoTelephone).all()

        return result

    def get_all_user_telephone_record(self):
        """

        :return: List< [from_telephone_id+to_telephone_id, from_telephone_id, to_telephone_id, List(record_datetime) ] >
        """
        mysql_session: Session = self.mysql_session()
        result_list = mysql_session.query(TbTelephoneRecord.from_telephone_id,
                                          TbTelephoneRecord.to_telephone_id,
                                          func.group_concat(TbTelephoneRecord.record_datetime)).group_by(
            TbTelephoneRecord.from_telephone_id, TbTelephoneRecord.to_telephone_id).all()
        result = [(str(r[0]) + ">" + str(r[1]), r[0], r[1], r[2].split(",")) for r in result_list]
        return result

    def get_all_personal_content(self):
        """

        :return: List< [from_telephone_id+to_telephone_id, from_telephone_id, to_telephone_id, List(record_datetime) ] >
        """
        mysql_session: Session = self.mysql_session()

        result_list = mysql_session.query(TbContentPersonal.from_app_user_id,
                                          TbContentPersonal.to_app_user_id,
                                          func.group_concat(TbContentPersonal.keywords, SEPARATOR="!@#@!"),
                                          func.group_concat(TbContentPersonal.content, SEPARATOR="!@#@!"),
                                          func.group_concat(TbContentPersonal.record_datetime, SEPARATOR="!@#@!"),
                                          ).group_by(
            TbContentPersonal.from_app_user_id, TbContentPersonal.to_app_user_id).all()
        # result = [[str(r[0]) + ">" + str(r[1]), r[0], r[1], r[2].split("!@#@!")] for r in result_list]
        result = []
        for r in result_list:
            rr = []
            for k, c, d in zip(r[2].split("!@#@!"), r[3].split("!@#@!"), r[4].split("!@#@!")):
                rr.append({
                    "keywords": k,
                    "content": c,
                    "record_datetime": d
                })
            result.append((str(r[0]) + ">" + str(r[1]), r[0], r[1], rr))
        return result

    # ----------------------------InitSpace End--------------------------------------------

    def get_user_telephones(self, card_id=None):
        """
        获取该人的所有手机号，不指定即返回搜索
        :param card_id:
        :return:
        """
        mysql_session = self.mysql_session()
        if card_id:
            r = mysql_session.query(TbInfoTelephone).join(TbInfoUser).filter(TbInfoUser.card_id == card_id).all()
        else:
            r = mysql_session.query(TbInfoTelephone).join(TbInfoUser).all()
        mysql_session.close()
        return r

    def get_personal_app_info(self, card_id=None):
        mysql_session: Session = self.mysql_session()

        # print(mysql_session)

        if card_id:
            r = mysql_session.query(TbInfoAppUser).join(TbInfoUser).filter(
                TbInfoUser.card_id == card_id).all()

        else:
            r = mysql_session.query(TbInfoAppUser).join(TbInfoUser).join(TbInfoApp).all()
        mysql_session.close()

        return r

    def get_telephone_record(self, filter=None):
        mysql_session = self.mysql_session()
        # print(mysql_session)
        if filter:
            r = mysql_session.query(TbTelephoneRecord).filter_by(**filter).all()
        else:
            r = mysql_session.query(TbTelephoneRecord).all()
        mysql_session.close()
        return r


if __name__ == '__main__':

    # result = UserService().get_user_telephones("vtyCeAkHhl")
    # for i in result:
    #     print(i)
    # print(model_to_dict(result))
    # r = UserService().get_personal_app_info({"id": 1111})
    # print(model_to_dict(r))
    Session = MysqlConnect("10.66.10.234:3306", "root", "234").connect("final")
    # r = Session().execute("select * from A").all()
    # print(r[0][0])
    # d = []
    # # print(r[0][0].split("'"))
    # #
    # # print(json.dumps([{"A": r[0][0]}],ensure_ascii=False))
    # print('\\"'.join(r[0][0].split('"')))
    # d.append({"A": "\\'".join(r[0][0].split("'"))})
    # rr_str = json.dumps(d, ensure_ascii=False)
    # print(rr_str)
    # print(d)
    # rr = json.dumps(d, ensure_ascii=False)
    # print(rr)
    # r_dic = json.loads(rr)
    # print(r_dic)
    # print(r_dic[0]["A"])

    r = UserService(Session).get_all_personal_content()
    for i in r:
        print(i)
        print(i[3])
        s = str(i[3])
        print(s)
        print(eval(s))
        break
    rr = []
    rr.append({
        "keywords": "11",
        "content": "11",
        "record_datetime": "d"
    })
    print(rr)
    print({
        "keywords": "11",
        "content": "11",
        "record_datetime": "d"
    })
    # print(time.time())
    # r = UserService(Session).get_personal_app_info()
    # print(model_json.model_to_dict(r))
    # print('*' * 30)
    # r = UserService(Session).get_telephone_record()
    # print(r)
    # print(model_json.model_to_dict(r))
    # # print(model_to_dict(r))
    # print(time.time())
    # print(json.dumps(model_to_dict(r)))
    # r = UserService(Session).get_all_user_telephone_record()
    # print(r)
