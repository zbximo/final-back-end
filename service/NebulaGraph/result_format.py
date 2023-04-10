# -*- encoding: utf-8 -*-
# @ModuleName: result_formate
# @Author: ximo
# @Time: 2023/3/30 15:14
import json

from nebula3.gclient.net import ConnectionPool, Session
from nebula3.Config import Config
import pandas as pd
from typing import Dict
from nebula3.data.ResultSet import ResultSet
from nebula3.data.DataObject import PathWrapper, Node

from service.NebulaGraph.nebula_connector import NebulaConnector

"""
format_path: col_key -> p
format_node: col_key -> v 
format_relation: col_key -> e 只查询关系 节点只有ID
根据返回值定的
node:
{
        'id': 'N1',
        'text': '侯亮平',
        // 下面这个前端加 
        'color': '#ec6941',
        'borderColor': '#ff875e',
        'data': {'isGoodMan': true, 'sexType': '男'},
        // eslint-disable-next-line no-undef
        // 下面这个前端加 
        'innerHTML': '<div class="c-my-node" style="background-image: url(' + this.wx_logo + ');border:#ff875e solid 3px;"><div class="c-node-name" style="color:#ff875e">侯亮平</div></div>'
        // 'innerHTML': '<div class="c-my-node" style="background-image: url(https://dss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=2308340537,462224207&fm=58&app=83&f=JPEG?w=250&h=250&s=EC708F46DA96B89CB69D5DDA0300D014);border:#ff875e solid 3px;"><div class="c-node-name" style="color:#ff875e">侯亮平</div></div>'
}
link:
{
      'from': 'N6',
      'to': 'N3',
      'text': '师生',
      'color': '#d2c0a5',
      'fontColor': '#d2c0a5',
      'data': {'type': '师生'}
}
"""


def format_path(result: ResultSet):
    """
    返回{
        "nodes": nodes,
        "lines": lines
    }
    :param result: 路径查询结果
    :return:
    """
    assert result.is_succeeded()
    columns = result.keys()

    d: Dict = {}
    for col_num in range(result.col_size()):
        col_name = columns[col_num]
        col_list = result.column_values(col_name)
        # print(col_name, col_list)
        d[col_name] = [x.cast() for x in col_list]
    nodes = []
    lines = []
    for k, v in d.items():
        for i in v:
            # print(i.__dict__)
            i: PathWrapper
            for node in i.nodes():
                n_tmp = node.properties(node.tags()[0])
                data = dict()
                for k, v in n_tmp.items():
                    data[k] = v.cast()

                data.pop("id")
                n = {
                    'id': n_tmp["id"].cast(),
                    'text': '',
                    'color': '#ec6941',
                    'borderColor': '#ff875e',
                    'data': {
                        "type": node.tags()[0],
                        "data": data
                    },
                }
                if n not in nodes:
                    nodes.append(n)
                # nodes.append(n)
            # print(t.properties(t.tags()[0]))
            for re in i.relationships():
                link_tmp = re.properties()
                data = dict()
                for k, v in link_tmp.items():
                    data[k] = v.cast()
                    if "from" in k:
                        f = v.cast()
                    if "to" in k:
                        t = v.cast()
                data.pop("id")
                link = {
                    'from': f,
                    'to': t,
                    'text': '',
                    'color': '#d2c0a5',
                    'fontColor': '#d2c0a5',
                    'data': {
                        "type": re.edge_name(),
                        "data": data
                    }
                }
                if link not in lines:
                    lines.append(link)
                # print(t.edge_name(), t.properties()["id"])
            # print(t.properties(t.()[0]), end=" *** ")

            # r: Vertex = t.__dict__["_value"]
            # print(t.tags(), t.get_id(), t.__dict__["_value"])
            # break
            # print('*' * 20)
            # print(i.start_node(), i.length(), i.nodes())
        break
    # return pd.DataFrame()
    # print(pd.DataFrame.from_dict(d))
    # print(len(nodes))
    # print(nodes)
    # print(lines)
    # result_pd = pd.DataFrame.from_dict(d)
    # print(result_pd)
    # return result_pd
    return {
        "nodes": nodes,
        "lines": lines
    }


def format_node(result: ResultSet):
    """
    返回{
        "nodes": nodes,
    }
    :param result: 节点查询结果
    :return:
    """
    assert result.is_succeeded()
    columns = result.keys()

    d: Dict = {}
    for col_num in range(result.col_size()):
        col_name = columns[col_num]
        col_list = result.column_values(col_name)
        # print(col_name, col_list)
        d[col_name] = [x.cast() for x in col_list]
    nodes = []
    for k, v in d.items():
        for i in v:
            i: Node
            n_tmp = i.properties(i.tags()[0])
            data = dict()
            for k, v in n_tmp.items():
                data[k] = v.cast()
            data.pop("id")
            n = {
                'id': n_tmp["id"].cast(),
                'text': '',
                'color': '#ec6941',
                'borderColor': '#ff875e',
                'data': {
                    "type": i.tags()[0],
                    "data": data
                },
            }
            nodes.append(n)
        break
    print("format nodes: ", nodes)
    return nodes


if __name__ == '__main__':
    ng_connection_pool = NebulaConnector("10.66.10.234", 9669, "root", "nebula").connect()
    ng_session: Session = ng_connection_pool.get_session("root", "nebula")
    ng_session.execute("USE test_final")
    # # 路径查询
    # nosql = r"""match p=(v:NodeUserInfo{{card_id:"{}"}})-[e*1..3]->(v2) return p limit 10""".format("Wg6iJHcszX")
    # result = ng_session.execute(nosql)
    # print(format_path(result))

    # 节点查询
    nosql = r"""match (v:NodeUserInfo{{card_id:"{}"}}) return v limit 1""".format("Wg6iJHcszX")
    print(nosql)
    result = ng_session.execute(nosql)
    print(format_node(result))
    ng_session.release()
