# -*- encoding: utf-8 -*-
# @ModuleName: Response
# @Author: ximo
# @Time: 2023/3/28 13:45
from flask import jsonify


class CodeNumber:
    Success = 1
    ERROR = 0


class ResponseData:
    def __init__(self, code=CodeNumber.Success, msg="success", data=None):
        self.dic = {
            "code": code,
            "msg": msg,
        }
        if data:
            self.dic['data'] = data

    def to_json(self):
        print(self.dic)
        res = jsonify(self.dic)
        return res
