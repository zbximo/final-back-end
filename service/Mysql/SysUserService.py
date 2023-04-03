# -*- encoding: utf-8 -*-
# @ModuleName: operate
# @Author: ximo
# @Time: 2023/3/3 21:43


from model import *
from db_connector import MysqlConnect
from utils.Response import CodeNumber


# # 每次执行数据库操作时，都需要创建一个session
#
# obj1 = TbInfoUser(user_name="test", user_card_id="111")
# session.add(obj1)
#
# # 提交事务
# session.commit()
# # 关闭session
# session.close()


class SysUserService:
    def __init__(self, mysql_session):
        self.mysql_session = mysql_session
        pass

    def query_sys_user(self, filter):
        mysql_session = self.mysql_session()
        return mysql_session.query(TbSysUser).filter_by(**filter).all()

    def update_sys_user(self, update_info, filter):
        mysql_session = self.mysql_session()
        result = mysql_session.query(TbSysUser).filter_by(**filter).update(update_info)
        mysql_session.commit()
        mysql_session.close()
        return result

    def login(self, data):
        res = {
            "code": CodeNumber.ERROR
        }
        mysql_session = self.mysql_session()
        r = mysql_session.query(TbSysUser).filter(TbSysUser.account == data["account"])
        if r.first():
            r1 = r.filter(TbSysUser.pwd == data["pwd"])
            if r1.first():
                res["code"] = CodeNumber.ERROR
                res["msg"] = "登陆成功"
            else:
                res["msg"] = "密码错误"
        else:
            res["msg"] = "账号不存在"
        return res


if __name__ == '__main__':
    # data = TbSysUser(sys_user_id=2)
    filter = {
        "account": "2",
        "pwd": "222"

    }

    update_info = {
        "pwd": "222"

    }

    Session = MysqlConnect("10.66.10.234:3306", "root", "234").connect("final")
    SUS = SysUserService(Session)
    r = SUS.login(filter)
    print(r)
    r = SUS.login(filter)
    print(r)
    # r = SysUserService().update_sys_user(update_info, filter)
    # r = SysUserService().query_sys_user(filter=up)
    #
    # for i in r:
    #     print(i.sys_user_id)
