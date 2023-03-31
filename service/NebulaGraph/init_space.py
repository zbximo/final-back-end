# -*- encoding: utf-8 -*-
# @ModuleName: init_space
# @Author: ximo
# @Time: 2023/3/31 15:40
import inspect
import time

from service.NebulaGraph.nebula_connector import NebulaConnector
import Nodes
import Relationships
from nebula3.gclient.net import Session

from nebula_connector import NebulaConnector
from result_format import format_path


class InitSpace:
    def __init__(self, space_name):
        connection_pool = NebulaConnector("10.66.10.234", 9669, "root", "nebula").connect()
        self.tag_list = self.get_edge_tag_list(Nodes)
        self.edge_list = self.get_edge_tag_list(Relationships)
        self.connection_pool = connection_pool
        self.space_name = space_name
        self.create_all()

    def create_all(self):
        self.create_space()
        time.sleep(1)
        self.create_tags()
        self.create_edges()

    def create_space(self):
        ng_session: Session = self.connection_pool.get_session("root", "nebula")
        ng_session.execute("CREATE SPACE IF NOT EXISTS {} (vid_type=FIXED_STRING(64)); ".format(self.space_name))
        ng_session.execute("CLEAR SPACE {};".format(self.space_name))
        ng_session.release()

    def get_edge_tag_list(self, _class):
        class_obj = []
        tag_list = []
        for name, obj in inspect.getmembers(_class):
            if inspect.isclass(obj):
                class_obj.append(obj)
        for cls in class_obj:
            # print(cls)
            props = []
            class_name = cls.__name__
            for name, value in cls.__annotations__.items():
                if isinstance(value, str):
                    # 如果类型注释是字符串，则将其转换为类型对象
                    value = eval(value)
                _type = value.__name__
                if _type != "int":
                    _type = "string"
                props.append([name, _type])
            tag_list.append({"name": class_name, "prop": props})

        return tag_list

    def create_tags(self):
        ng_session: Session = self.connection_pool.get_session("root", "nebula")
        ng_session.execute("USE {}".format(self.space_name))
        # for tag in self.tag_list:
        #     ng_session.execute("CREATE TAG IF NOT EXISTS player(name string, age int);")
        for tag in self.tag_list:
            nosql = "CREATE TAG IF NOT EXISTS {} (".format(tag["name"])
            for prop in tag["prop"]:
                nosql += (prop[0] + " " + prop[1] + ",")
            nosql = nosql[:-1] + " )"
            # print(nosql)
            r = ng_session.execute(nosql)
            # print(r.is_succeeded())
            # ng_session.execute("CREATE EDGE IF NOT EXISTS {}(degree int);".format(edge["name"]))
        ng_session.release()

    def create_edges(self):
        ng_session: Session = self.connection_pool.get_session("root", "nebula")
        ng_session.execute("USE {}".format(self.space_name))

        for edge in self.edge_list:
            nosql = "CREATE EDGE IF NOT EXISTS {} (".format(edge["name"])
            for prop in edge["prop"]:
                nosql += (prop[0] + " " + prop[1] + ",")
            nosql = nosql[:-1] + " )"
            # print(nosql)
            r = ng_session.execute(nosql)
            # print(r.is_succeeded())
            # ng_session.execute("CREATE EDGE IF NOT EXISTS {}(degree int);".format(edge["name"]))
        ng_session.release()


class MyClass:
    my_int: int
    my_str: str
    my_list: list
    my_dict: dict


if __name__ == '__main__':
    IS = InitSpace("test_final")
    IS.create_tags()
