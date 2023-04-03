# -*- encoding: utf-8 -*-
# @ModuleName: model2json
# @Author: ximo
# @Time: 2023/3/28 11:12
import datetime

from sqlalchemy.orm import class_mapper

from service.Mysql.db_connector import MysqlConnect
from service.Mysql.model import *


def model_to_dict(result):
    if result is None:
        return None
    if isinstance(result, list):
        if len(result) == 0:
            return None
        model = result[0]
        columns = [c for c in class_mapper(model.__class__).columns]
        result_dict = []

        for r in result:
            dic = {}
            for c in columns:
                c_type = str(c.type)
                if c_type == "DATETIME":
                    dic[c.key] = datetime.datetime.strftime(getattr(r, c.key), "%Y-%m-%d %H:%M:%S")
                elif c_type == "DATE":
                    dic[c.key] = datetime.datetime.strftime(getattr(r, c.key), "%Y-%m-%d")
                else:
                    dic[c.key] = getattr(r, c.key)
            result_dict.append(dic)
        # result_dict = [dict((c, getattr(r, c.key)) for c in columns) for r in result]
    else:
        model = result
        columns = [c for c in class_mapper(model.__class__).columns]
        result_dict = {}
        for c in columns:
            c_type = str(c.type)
            # print(c.type == "DATETIME")
            if c_type == "DATETIME":
                result_dict[c.key] = datetime.datetime.strftime(getattr(model, c.key), "%Y-%m-%d %H:%M:%S")
            elif c_type == "DATE":
                result_dict[c.key] = datetime.datetime.strftime(getattr(model, c.key), "%Y-%m-%d")
            else:
                result_dict[c.key] = getattr(model, c.key)
        # result_dict = dict((c, getattr(model, c)) for c in columns)
    return result_dict


def dict_to_model(obj_db, data):
    for col in obj_db.__class__.__table__.columns:
        key = col.name
        col_type = col.type
        if key in data:
            if col_type == "DATETIME":
                setattr(obj_db, key, data[key].strptime("%Y-%m-%d %H:%M:%S"))
            elif col_type == "DATE":
                setattr(obj_db, key, data[key].strptime("%Y-%m-%d"))
            else:
                setattr(obj_db, key, data[key])
    # for key in obj_db.__class__.__dict__.keys():
    #     if key in data:
    #         if "date" in key:
    #             setattr(obj_db, key, data[key].strptime("%Y-%m-%d %H:%M:%S"))
    #         else:
    #             setattr(obj_db, key, data[key])

    return obj_db


# def serialize(model):
#     columns = [c.key for c in class_mapper(model.__class__).columns]
#     return dict((c, getattr(model, c)) for c in columns)


if __name__ == '__main__':
    session = MysqlConnect("10.66.10.234:3306", "root", "234").connect("final")
    mysql_session = session()
    model_r = mysql_session.query(TbSysUser).limit(1).all()
    print(model_to_dict(model_r))
    # for i in TbTelphoneRecord.__table__.columns:
    #     print(i.type, i.name)
    #
    # data = {
    #     "sys_user_id": 1,
    #
    # }
    # print(model_to_dict(dict_to_model(TbSysUser(), data)))
