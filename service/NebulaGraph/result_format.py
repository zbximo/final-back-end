# -*- encoding: utf-8 -*-
# @ModuleName: result_formate
# @Author: ximo
# @Time: 2023/3/30 15:14
from nebula3.gclient.net import ConnectionPool
from nebula3.Config import Config
import pandas as pd
from typing import Dict
from nebula3.data.ResultSet import ResultSet
from nebula3.data.DataObject import PathWrapper


def format_path(result: ResultSet) -> pd.DataFrame:
    """
    build list for each column, and transform to dataframe
    """
    assert result.is_succeeded()
    columns = result.keys()

    d: Dict = {}
    for col_num in range(result.col_size()):
        col_name = columns[col_num]
        col_list = result.column_values(col_name)
        # print(col_name, col_list)
        d[col_name] = [x.cast() for x in col_list]

    for k, v in d.items():
        for i in v:
            # print(i.__dict__)
            i: PathWrapper
            # for t in i.nodes():
                # print(t.properties(t.tags()[0]))
            for t in i.relationships():
                print(t.properties())
                # print(t.properties(t.()[0]), end=" *** ")

                # r: Vertex = t.__dict__["_value"]
                # print(t.tags(), t.get_id(), t.__dict__["_value"])
                # break
            # print('*' * 20)
            # print(i.start_node(), i.length(), i.nodes())
        break
    # return pd.DataFrame()
    # print(pd.DataFrame.from_dict(d))
    result_pd = pd.DataFrame.from_dict(d)
    print(result_pd)
    return result_pd
