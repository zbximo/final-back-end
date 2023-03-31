# -*- encoding: utf-8 -*-
# @ModuleName: model
# @Author: ximo
# @Time: 2023/3/30 16:31

# coding: utf-8


# class TbInfoApp:
#     __tablename__ = 'tb_info_app'
#     __table_args__ = {'comment': '应用表，包含微信、QQ、推特、电话等'}
#
#     id: str
#     app_name: str
#     create_datetime: str


class NodeUserInfo:
    __NodeName__ = 'UserInfo'
    __type__ = "Node"
    id: str
    name: str
    card_id: str
    birthday: str
    sex: str


class NodeAppUserInfo:
    __NodeName__ = 'AppUserInfo'
    __type__ = "Node"

    id: str
    user_id: int  # 连接NodeUserInfo: id，不显示
    app_id: int
    app_name: int  # app名字,根据app_id查出来
    app_user_account: str
    app_user_nickname: str


class NodeGroupInfo:
    __NodeName__ = 'GroupInfo'
    __type__ = "Node"
    id: str
    group_id: str  # 组的id
    group_name: str
    app_id: int
    app_name: int  # app名字,根据app_id查出来


class NodeTelephoneInfo:
    __NodeName__ = 'TelephoneInfo'
    __type__ = "Node"
    id: str
    user_id: int  # 连接NodeUserInfo: id，不显示
    telephone: str
