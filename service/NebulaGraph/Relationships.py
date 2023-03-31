# -*- encoding: utf-8 -*-
# @ModuleName: model
# @Author: ximo
# @Time: 2023/3/30 16:31

# coding: utf-8


class RelationAppUser:
    __ReName__ = 'RelationAppUser'
    __type__ = "Relation"
    __args__ = "边：关联 用户信息 和 用户应用信息。"

    id: str
    # NodeUserInfo-->NodeAppUserInfo
    from_user: int  # NodeAppUserInfo.user_id == NodeUserInfo.id
    to_app: int  # NodeAppUserInfo.id


class RelationUserAppGroup:
    __ReName__ = 'RelationUserAppGroup'
    __type__ = "Relation"
    __args__ = "边：关联 用户应用信息 和 应用群组信息。 主要存储用户在群组里的聊天记录"
    id: str
    # NodeAppUserInfo-->NodeGroupInfo
    from_app_user_id: int  # NodeAppUserInfo.user_id
    to_app_group_id: int  # NodeGroupInfo.id
    contents: dict
    """
    [
        {
             "content": str,
             "keywords": str,
             "datetime": str
        }
    ]
    """


class RelationTelephoneInfo:
    __ReName__ = 'RelationUserTelephone'
    __type__ = "Relation"
    __args__ = "边：关联 用户信息 和 电话信息。 "

    id: str
    # NodeUserInfo-->NodeTelephoneInfo
    from_user_id: int  # NodeUserInfo.id
    to_telephone_id: int  # NodeTelephoneInfo.id


class RelationPersonalContent:
    __ReName__ = 'RelationPersonalContent'
    __type__ = "Relation"
    # __args__ = {'comment': '个人间不同应用的聊天记录'}
    __args__ = "边：关联 用户应用信息 和 用户应用信息。用户个人聊天记录 "

    id: str
    # NodeAppUserInfo-->NodeAppUserInfo
    from_app_user_id: int  # NodeAppUserInfo.id
    to_app_user_id: int  # NodeAppUserInfo.id
    contents: dict
    """
    [
        {
             "content": str,
             "keywords": str,
             "datetime": str
        }
    ]
    """


class RelationTelephoneRecord:
    __ReName__ = 'RelationTelephoneRecord'
    __type__ = "Relation"
    # __args__ = {'comment': '个人间电话记录'}
    __args__ = "边：关联 用户电话信息 和 用户电话信息。用户个人电话记录 "

    id: str
    # NodeTelephoneInfo-->NodeTelephoneInfo
    from_telephone_id: int  # NodeTelephoneInfo.id
    to_telephone_id: int  # NodeTelephoneInfo.id
    records: dict
    """
    [
        {
             "datetime": str
        }
    ]
    """
