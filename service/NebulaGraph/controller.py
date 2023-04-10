# -*- encoding: utf-8 -*-
# @ModuleName: controller
# @Author: ximo
# @Time: 2023/4/9 21:07
from nebula3.gclient.net import Session

from service.NebulaGraph import result_format
from service.NebulaGraph.nebula_connector import NebulaConnector


class Controller:
    def __init__(self, space_name, ng_connection_pool):
        # ng_connection_pool = NebulaConnector("10.66.10.234", 9669, "root", "nebula").connect()
        self.ng_connection_pool = ng_connection_pool
        self.space_name = space_name

    def get_n_r_by_card_id(self, card_id, rootID=False):
        ng_session: Session = self.ng_connection_pool.get_session("root", "nebula")
        ng_session.execute("USE {}".format(self.space_name))
        nosql = r"""match p=(v:NodeUserInfo{{card_id:"{}"}})-[e*1]->(v2) return p limit 10""".format(card_id)
        print(nosql)
        result = ng_session.execute(nosql)

        format_n_r = result_format.format_path(result)
        if rootID:
            nosql = r"""match (v:NodeUserInfo{{card_id:"{}"}}) return v limit 1""".format(card_id)
            result = ng_session.execute(nosql)
            # print(result)
            r = result_format.format_node(result)
            if len(r) == 0:
                return None
            format_n_r["rootId"] = r[0]["id"]

        ng_session.release()
        return format_n_r

    def get_n_r_by_node_id(self, node_id):
        ng_session: Session = self.ng_connection_pool.get_session("root", "nebula")
        ng_session.execute("USE {}".format(self.space_name))
        node_tag = node_id.split("_")
        nosql = r"""match p=(v:{}{{id:"{}"}})-[e*1]->(v2) return p limit 10""".format(node_tag, node_id)
        print(nosql)
        result = ng_session.execute(nosql)
        format_n_r = result_format.format_path(result)
        ng_session.release()
        return format_n_r

    def get_r_by_node_id(self, node_id):
        ng_session: Session = self.ng_connection_pool.get_session("root", "nebula")
        ng_session.execute("USE {}".format(self.space_name))
        node_tag = node_id.split("_")
        nosql = r"""match p=(v:{}{{id:"{}"}})-[e*1]->(v2) return p limit 10""".format(node_tag, node_id)
        result = ng_session.execute(nosql)
        format_n_r = result_format.format_path(result)
        ng_session.release()
        return format_n_r


if __name__ == '__main__':
    ng_connection_pool = NebulaConnector("10.66.10.234", 9669, "root", "nebula").connect()

    c = Controller("test_final", ng_connection_pool)
    c.get_n_r_by_card_id("Wg6iJHcszX", True)
