# -*- encoding: utf-8 -*-
# @ModuleName: controller
# @Author: ximo
# @Time: 2023/4/9 21:07
from nebula3.gclient.net import Session

from service.NebulaGraph.nebula_connector import NebulaConnector
import result_format
class Controller:
    def __init__(self, space_name):
        ng_connection_pool = NebulaConnector("10.66.10.234", 9669, "root", "nebula").connect()
        self.ng_connection_pool = ng_connection_pool
        self.space_name = space_name

    def get_by_card_id(self, card_id):
        ng_session: Session = self.ng_connection_pool.get_session("root", "nebula")
        ng_session.execute("USE {}".format(self.space_name))
        nosql = r"""match p=(v:NodeUserInfo{{card_id:"{}"}})-[e*1..3]->(v2) return p limit 10""".format(card_id)
        print(nosql)
        result = ng_session.execute(nosql)
        print(result_format.format_path(result))


if __name__ == '__main__':
    c = Controller("test_final")
    c.get_by_card_id("Wg6iJHcszX")
