# # -*- encoding: utf-8 -*-
# # @ModuleName: test
# # @Author: ximo
# # @Time: 2023/3/28 16:19
# import nebula3
# from nebula3.gclient.net import ConnectionPool
# from nebula3.Config import Config
# import pandas as pd
# from typing import Dict
# from nebula3.data.ResultSet import ResultSet
# from nebula3.data.DataObject import PathWrapper
# from nebula3.common.ttypes import Vertex, Edge
#
#
# def result_to_df(result: ResultSet) -> pd.DataFrame:
#     """
#     build list for each column, and transform to dataframe
#     """
#     assert result.is_succeeded()
#     columns = result.keys()
#     d: Dict[str, list] = {}
#     for col_num in range(result.col_size()):
#         col_name = columns[col_num]
#         col_list = result.column_values(col_name)
#         d[col_name] = [x.cast() for x in col_list]
#     for k, v in d.items():
#         for i in v:
#             # print(i.__dict__)
#             i: PathWrapper
#             for t in i.nodes():
#                 t.properties("player")
#                 print(t.properties("player"))
#                 # r: Vertex = t.__dict__["_value"]
#                 # print(t.tags(), t.get_id(), t.__dict__["_value"])
#                 break
#             print('*' * 20)
#             # print(i.start_node(), i.length(), i.nodes())
#     return pd.DataFrame()
#     # print(d)
#     # return pd.DataFrame.from_dict(d, columns=columns)
#
#
# # define a config
# config = Config()
#
# # init connection pool
# ng_connection_pool = ConnectionPool()
#
# # if the given servers are ok, return true, else return false
# ok = ng_connection_pool.init([('10.66.10.234', 9669)], config)
#
# x = ng_connection_pool.get_session("root", "nebula")
# print(x)
# x = ng_connection_pool.get_session("root", "nebula")
#
# print(x)
# # option 2 with session_context, session will be released automatically
# # with ng_connection_pool.session_context('root', 'nebula') as session:
# #     session.execute('USE basketball')
# #     result = session.execute('MATCH p=(v:player{name:"Tim Duncan"})-->(v2) RETURN p')
# #     df = result_to_df(result)
# #     # print(df)
# #
# # # close the pool
# # ng_connection_pool.close()
import json

d = {
    'd': '"啊"啊啊啊\'\'',
}
d = '[{"keywords": "f4BX3UwjgN", "content": "Navicat allows you to transfer data from one database and/or schema to another with detailed analytical process. user\'s request.The On Startup feature allows you to control what tabs appear when you launch Navicat.", "datetime": "2020-06-12 20:31:54"}]'
r = json.loads(d)
print(r)
