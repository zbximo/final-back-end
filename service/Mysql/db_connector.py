# -*- encoding: utf-8 -*-
# @ModuleName: db_connector
# @Author: ximo
# @Time: 2023/3/27 20:34
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from service.Mysql.model import *


class MysqlConnect:
    def __init__(self, host, user, pwd):
        self.host = host
        self.user = user
        self.pwd = pwd

    def connect(self, db_name):
        # URL = "mysql+pymysql://root:123456@8.130.78.75:3306/final"
        URL = "mysql+pymysql://{}:{}@{}/{}".format(self.user, self.pwd, self.host, db_name)
        print(URL)
        try:
            engine = create_engine(URL, max_overflow=0, pool_size=8)
            Session = sessionmaker(bind=engine)
            return Session
        except:
            return None
        # 每次执行数据库操作时，都需要创建一个session


if __name__ == '__main__':
    session = MysqlConnect("8.130.78.75:3306", "root", "123456").connect("final")
    db_session = session()

    # print(db_session.query(TbSysUser).limit(10).all())
