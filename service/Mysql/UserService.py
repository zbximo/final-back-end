# -*- encoding: utf-8 -*-
# @ModuleName: UserService
# @Author: ximo
# @Time: 2023/3/28 14:54
import json
import time

from app import Session
from model import *
from utils.model_json import *


class UserService:
    def __init__(self):
        pass

    def get_user_telephones(self, card_id=None):
        """
        获取该人的所有手机号，不指定即返回搜索
        :param card_id:
        :return:
        """
        db_session = Session()
        if card_id:
            r = db_session.query(TbInfoTelephone).join(TbInfoUser).filter(TbInfoUser.card_id == card_id).all()
        else:
            r = db_session.query(TbInfoTelephone).join(TbInfoUser).all()
        db_session.close()
        return r

    def get_personal_app_info(self, card_id=None):
        db_session = Session()
        print(db_session)
        if card_id:
            r = db_session.query(TbInfoAppUser).join(TbInfoUser).filter(
                TbInfoUser.card_id == card_id).all()
        else:
            r = db_session.query(TbInfoAppUser).join(TbInfoUser).join(TbInfoApp).all()
        db_session.close()
        print(111)
        return r

    def get_telephone_record(self, filter=None):
        db_session = Session()
        print(db_session)
        if filter:
            r = db_session.query(TbTelephoneRecord).filter_by(**filter).all()
        else:
            r = db_session.query(TbTelephoneRecord).all()
        db_session.close()
        return r


if __name__ == '__main__':
    # result = UserService().get_user_telephones("vtyCeAkHhl")
    # for i in result:
    #     print(i)
    # print(model_to_dict(result))
    # r = UserService().get_personal_app_info({"id": 1111})
    # print(model_to_dict(r))
    print(time.time())
    r = UserService().get_personal_app_info("vtyCeAkHhl")
    print(time.time())
    print('*' * 30)
    r = UserService().get_telephone_record()
    # print(model_to_dict(r))
    print(time.time())
    # print(json.dumps(model_to_dict(r)))
