# -*- encoding: utf-8 -*-
# @ModuleName: opreator
# @Author: ximo
# @Time: 2023/3/30 15:07
import time

from nebula3.gclient.net import Session

from nebula_connector import NebulaConnector
from result_format import format_path


class Operator:
    def __init__(self, space_name, connection_pool):
        # self.ng_session = connection_pool.get_session("root", "nebula")
        self.connection_pool = connection_pool
        self.space_name = space_name
        # self.ng_session.execute("Use {}".format(self.space_name))

    def insert_nodes(self, data):
        """

        :param data: nodes
        :return:
        """
        ng_session: Session = self.connection_pool.get_session("root", "nebula")
        # ng_session.execute("USE basketball")
        ng_session.execute("USE {}".format(self.space_name))
        result = ng_session.execute('MATCH p=(v:player{name:"Tim Duncan"})-[e*1]->(v2) RETURN p')
        format_path(result)
        ng_session.release()

    def insert_relation(self, data):
        """

        :param data: relation
        :return:
        """
        pass

    def find_all(self):
        # connection_pool = NebulaConnector("10.66.10.234", 9669, "root", "nebula").connect()
        ng_session: Session = self.connection_pool.get_session("root", "nebula")
        # ng_session.execute("USE basketball")
        ng_session.execute("USE {}".format(self.space_name))
        result = ng_session.execute('MATCH p=(v:player{name:"Tim Duncan"})-[e*1]->(v2) RETURN p')
        format_path(result)
        ng_session.release()
        # time.sleep(10)


if __name__ == '__main__':
    connection_pool = NebulaConnector("10.66.10.234", 9669, "root", "nebula").connect()

    op = Operator("basketball", connection_pool)
    op.find_all()
    op.find_all()
