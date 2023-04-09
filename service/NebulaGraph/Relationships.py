# -*- encoding: utf-8 -*-
# @ModuleName: model
# @Author: ximo
# @Time: 2023/3/30 16:31

# coding: utf-8


class RelationAppUser:
    # TbInfoAppUser
    __ReName__ = 'RelationAppUser'
    __type__ = "Relation"
    __args__ = "边：关联 用户信息 和 用户应用信息。"

    id: str
    # NodeUserInfo-->NodeAppUserInfo
    from_user: str  # NodeAppUserInfo.user_id == NodeUserInfo.id   TbInfoAppUser.user_id
    to_app: str  # NodeAppUserInfo.id                              TbInfoAppUser.app_id


class RelationUserAppGroup:
    # TbInfoGroupUser
    __ReName__ = 'RelationUserAppGroup'
    __type__ = "Relation"
    __args__ = "边：关联 用户应用信息 和 应用群组信息。 主要存储用户在群组里的聊天记录"
    id: str
    # NodeAppUserInfo-->NodeGroupInfo
    from_app_user_id: str  # NodeAppUserInfo.id  TbInfoGroupUser.app_user_id
    to_app_group_id: str  # NodeGroupInfo.id    TbInfoGroupUser.group_id
    contents: list  # TbContentGroupUser---TbInfoGroupUser
    """
    [
        {
             "content": str,
             "keywords": str,
             "record_datetime": str
        }
    ]
    """


class RelationTelephoneInfo:
    # TbInfoTelephone
    __ReName__ = 'RelationUserTelephone'
    __type__ = "Relation"
    __args__ = "边：关联 用户信息 和 电话信息。 "

    id: str
    # NodeUserInfo-->NodeTelephoneInfo
    from_user_id: str  # NodeUserInfo.id       TbInfoTelephone.user_id
    to_telephone_id: str  # NodeTelephoneInfo.id  TbInfoTelephone.id


class RelationPersonalContent:
    # TbContentPersonal
    __ReName__ = 'RelationPersonalContent'
    __type__ = "Relation"
    # __args__ = {'comment': '个人间不同应用的聊天记录'}
    __args__ = "边：关联 用户应用信息 和 用户应用信息。用户个人聊天记录 "

    id: str
    # NodeAppUserInfo-->NodeAppUserInfo
    from_app_user_id: str  # NodeAppUserInfo.id    TbContentPersonal.from_app_user_id
    to_app_user_id: str  # NodeAppUserInfo.id    TbContentPersonal.to_app_user_id
    contents: list  # TbContentPersonal.other
    """
    [
        {
             "content": str,
             "keywords": str,
             "record_datetime": str
        }
    ]
    """


class RelationTelephoneRecord:
    # TbTelephoneRecord
    __ReName__ = 'RelationTelephoneRecord'
    __type__ = "Relation"
    # __args__ = {'comment': '个人间电话记录'}
    __args__ = "边：关联 用户电话信息 和 用户电话信息。用户个人电话记录 "

    id: str
    # NodeTelephoneInfo-->NodeTelephoneInfo
    from_telephone_id: str  # NodeTelephoneInfo.id   TbTelephoneRecord.from_telephone_id
    to_telephone_id: str  # NodeTelephoneInfo.id     TbTelephoneRecord.to_telephone_id
    records: dict
    """
    [
        {
             "record_datetime": str
        }
    ]
    """


class RelationDeliveryRecord:
    # TbTelephoneRecord
    __ReName__ = 'RelationDeliveryRecord'
    __type__ = "Relation"
    # __args__ = {'comment': '个人间电话记录'}
    __args__ = "边：关联 用户信息 和 用户信息。用户快递信息 "

    id: str
    # NodeUserInfo-->NodeUserInfo
    from_user_id: str  # NodeUserInfo.id
    to_user_id: str  # NodeUserInfo.id
    records: dict
    """
    [
        {
            "from_address": str,
            "to_address": str,
            "record_datetime": datetime
        }
    ]
    """


class RelationSearchRecord:
    # TbTelephoneRecord
    __ReName__ = 'RelationSearchRecord'
    __type__ = "Relation"
    # __args__ = {'comment': '个人间电话记录'}
    __args__ = "边：关联 用户APP信息 和 搜索信息。用户搜索信息 "

    id: str
    # NodeAPPUserInfo-->NodeSearchInfo
    from_app_user_id: str  # NodeAppUserInfo.id
    to_search_id: str  # NodeSearchInfo.id == NodeAppUserInfo.id
    records: dict
    """
    [
        {
             "content": str,
             "keywords": str,
             "record_datetime": str
        }
    ]
    """
