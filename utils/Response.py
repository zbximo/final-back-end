# -*- encoding: utf-8 -*-
# @ModuleName: Response
# @Author: ximo
# @Time: 2023/3/28 13:45
class CodeNumber:
    Success = 1
    ERROR = 0


class ResponseData:
    def __init__(self, code=CodeNumber.Success, msg="success", data=None):
        dic = {
            "code": code,
            "msg": msg,
        }
        if data:
            dic['data'] = data
