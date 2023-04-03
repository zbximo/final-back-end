# -*- encoding: utf-8 -*-
# @ModuleName: opreator
# @Author: ximo
# @Time: 2023/3/30 15:07
import time

from nebula3.gclient.net import Session

from service.NebulaGraph.nebula_connector import NebulaConnector
from result_format import format_path
from service.Mysql.UserService import UserService
from service.Mysql.db_connector import MysqlConnect
from utils.model_json import model_to_dict
from service.NebulaGraph.Nodes import *


class Operator:
    def __init__(self, space_name, ng_connection_pool):
        # self.ng_session = ng_connection_pool.get_session("root", "nebula")
        self.ng_connection_pool = ng_connection_pool
        self.space_name = space_name
        # self.ng_session.execute("Use {}".format(self.space_name))

    def insert_nodes(self, node_list: list):
        """

        :param node_list: List(Node)
        :return:
        """

        ng_session: Session = self.ng_connection_pool.get_session("root", "nebula")
        ng_session.execute("USE {}".format(self.space_name))
        items = self.get_item_type(node_list[0])
        print(items)
        # for node in node_list:
        #     break
            # nosql = """INSERT VERTEX t2 (name, age) VALUES "13":("n3", 12), "14":("n4", 8); """

        # result = ng_session.execute('MATCH p=(v:player{name:"Tim Duncan"})-[e*1]->(v2) RETURN p')
        # format_path(result)
        ng_session.release()

    def insert_relation(self, relation_list: list):
        """

        :param relation_list: relation
        :return:
        """
        pass

    def find_all(self):
        # ng_connection_pool = NebulaConnector("10.66.10.234", 9669, "root", "nebula").connect()
        ng_session: Session = self.ng_connection_pool.get_session("root", "nebula")
        # ng_session.execute("USE basketball")
        ng_session.execute("USE {}".format(self.space_name))
        result = ng_session.execute('MATCH p=(v:player{name:"Tim Duncan"})-[e*1]->(v2) RETURN p')
        format_path(result)
        ng_session.release()
        # time.sleep(10)

    def get_item_type(self, cls):
        result = {
            "class_name": "",
            "item": []
        }
        class_name = cls.__class__.__name__
        items = []
        for name, value in cls.__annotations__.items():
            if isinstance(value, str):
                # 如果类型注释是字符串，则将其转换为类型对象
                value = eval(value)
            _type = value.__name__
            items.append([name, _type])
        result["class_name"] = class_name
        result["item"] = items
        return result


if __name__ == '__main__':
    # ng_connection_pool = NebulaConnector("10.66.10.234", 9669, "root", "nebula").connect()
    #
    # op = Operator("basketball", ng_connection_pool)
    # op.find_all()
    # op.find_all()

    node = NodeUserInfo()
    node.__dict__["id"] = 1
    print(node.__dict__)
    Session = MysqlConnect("10.66.10.234:3306", "root", "234").connect("final")

    print(time.time())
    r = UserService(Session).get_personal_app_info()
    for i in r:
        print(i.__dict__)
    print(model_to_dict(r))
    # cls = NodeUserInfo()
    # class_name = cls.__class__.__name__
    # print(class_name)
    # for name, value in cls.__annotations__.items():
    #     if isinstance(value, str):
    #         # 如果类型注释是字符串，则将其转换为类型对象
    #         value = eval(value)
    #     _type = value.__name__
    #     print(name, _type)
