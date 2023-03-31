# -*- encoding: utf-8 -*-
# @ModuleName: nebula_connector
# @Author: ximo
# @Time: 2023/3/28 21:03

# -*- encoding: utf-8 -*-
# @ModuleName: test
# @Author: ximo
# @Time: 2023/3/28 16:19
import nebula3
from nebula3.gclient.net import ConnectionPool
from nebula3.Config import Config
import pandas as pd
from typing import Dict
from nebula3.data.ResultSet import ResultSet
from nebula3.data.DataObject import PathWrapper
from nebula3.common.ttypes import Vertex, Edge


class NebulaConnector:
    def __init__(self, ip, port, name, pwd):
        self.ip = ip
        self.port = port
        self.name = name
        self.pwd = pwd

    def connect(self):
        config = Config()

        connection_pool = ConnectionPool()

        # if the given servers are ok, return true, else return false
        ok = connection_pool.init([(self.ip, self.port)], config)
        if ok:
            return connection_pool
        else:
            return None
        # option 2 with session_context, session will be released automatically
        # with connection_pool.session_context('root', 'nebula') as session:
        #     # session
        #     session.execute('USE basketball')
        #     result = session.execute('MATCH p=(v:player{name:"Tim Duncan"})-->(v2) RETURN p')
        #     df = result_to_df(result)
        #     # print(df)


if __name__ == '__main__':
    config = Config()

    connection_pool = ConnectionPool()

    # if the given servers are ok, return true, else return false
    ok = connection_pool.init([("10.66.10.234", 9669)], config)
    session = connection_pool.get_session("root", "nebula")
    print(session)
    print(session)
    # print(connection_pool.connects())
