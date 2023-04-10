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
    # Mysql: TbInfoUser
    __NodeName__ = 'UserInfo'
    __type__ = "Node"
    id: str
    name: str
    card_id: str
    birthday: str
    sex: str
    address: str
    arrested: str
    score: float


class NodeAppUserInfo:
    # Mysql: TbInfoAppUser
    __NodeName__ = 'AppUserInfo'
    __type__ = "Node"

    id: str
    user_id: int  # 连接NodeUserInfo: id，不显示
    app_id: int
    app_name: str  # app名字,根据app_id查出来
    app_user_account: str
    app_user_nickname: str


class NodeGroupInfo:
    # TbInfoGroup
    __NodeName__ = 'GroupInfo'
    __type__ = "Node"
    id: str
    group_id: str  # 组的id
    group_name: str
    app_id: int
    app_name: str  # app名字,根据app_id查出来


class NodeTelephoneInfo:
    # TbInfoTelephone
    __NodeName__ = 'TelephoneInfo'
    __type__ = "Node"
    id: str
    user_id: int  # 连接NodeUserInfo: id，不显示
    telephone: str


class NodeSearchInfo:
    # TbSearch表 根据app_user_id distinct创建
    __NodeName__ = 'SearchInfo'
    __type__ = "Node"
    id: str  # 也为app_user_id
    app_user_id: int  # 连接NodeUserInfo: id，不显示
