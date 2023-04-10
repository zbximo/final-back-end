# -*- encoding: utf-8 -*-
# @ModuleName: mysql2ng
# @Author: ximo
# @Time: 2023/4/1 15:15
import json

from service.Mysql.UserService import UserService
from service.Mysql.db_connector import MysqlConnect
from utils import model_json
from service.NebulaGraph.Nodes import *
from service.NebulaGraph.Relationships import *
from service.Mysql.model import *


def fromTbInfoUser2NodeUserInfo(user_list):
    """

    :param user_list: List<TbInfoUser>
    :return:
    """
    result_dic = model_json.model_to_dict(user_list)
    if isinstance(result_dic, list):
        result_nodes = []

        for result in result_dic:
            node = NodeUserInfo()
            node.id = "NodeUserInfo_" + str(result["id"])
            node.name = result["name"]
            node.card_id = result["card_id"]
            node.birthday = result["birthday"]
            node.sex = "男" if result["sex"] == "M" else "女"
            node.address = result["address"]
            node.arrested = "否" if result["arrested"] == "N" else "是"
            node.score = result['score']
            result_nodes.append(node)
    else:
        result = result_dic
        node = NodeUserInfo()
        node.id = "NodeUserInfo_" + str(result["id"])
        node.name = result["name"]
        node.card_id = result["card_id"]
        node.birthday = result["birthday"]
        node.sex = "男" if result["sex"] == "M" else "女"
        node.address = result["address"]
        node.arrested = "否" if result["arrested"] == "N" else "是"
        node.score = result['score']
        result_nodes = node
    return result_nodes

    # r = UserService(Session).get_search_nodes()


def fromTbSearch2NodeSearchInfo(app_user_list):
    """

    :param app_user_list: List<int>
    :return:
    """
    # result_dic = model_json.model_to_dict(app_user_list)
    if isinstance(app_user_list, list):
        result_nodes = []
        for app_user_id in app_user_list:
            node = NodeSearchInfo()
            node.id = "NodeSearchInfo_" + str(app_user_id)
            node.app_user_id = app_user_id
            result_nodes.append(node)
    else:
        app_user_id = app_user_list
        node = NodeSearchInfo()
        node.id = "NodeSearchInfo_" + str(app_user_id)
        node.app_user_id = app_user_id
        result_nodes = node
    return result_nodes


def fromTbInfoAppUser2NodeAppUserInfo(app_user_list):
    """

    :param app_user_list: List<(TbInfoAppUser, TbInfoApp)>
    :return:
    """
    # result_dic = model_json.model_to_dict(app_user_list)
    if isinstance(app_user_list, list):
        result_nodes = []
        for app_user_model, app_model in app_user_list:
            app_user = model_json.model_to_dict(app_user_model)
            app_dict = model_json.model_to_dict(app_model)
            node = NodeAppUserInfo()
            node.id = "NodeAppUserInfo_" + str(app_user["id"])
            node.user_id = app_user["user_id"]
            node.app_user_account = app_user["app_user_account"]
            node.app_user_nickname = app_user["app_user_nickname"]
            node.app_id = app_user["app_id"]
            node.app_name = app_dict["app_name"]
            result_nodes.append(node)
    else:
        app_user_model, app_model = app_user_list
        app_user = model_json.model_to_dict(app_user_model)
        app_dict = model_json.model_to_dict(app_model)
        node = NodeAppUserInfo()
        node.id = "NodeAppUserInfo_" + str(app_user["id"])
        node.user_id = app_user["user_id"]
        node.app_user_account = app_user["app_user_account"]
        node.app_user_nickname = app_user["app_user_nickname"]
        node.app_id = app_user["app_id"]
        node.app_name = app_dict["app_name"]
        result_nodes = node
    return result_nodes


def fromTbInfoGroup2NodeGroupInfo(group_list):
    """

    :param app_user_list: List<(TbInfoGroup,TbInfoApp)>
    :return:
    """
    # result_dic = model_json.model_to_dict(app_user_list)
    if isinstance(group_list, list):
        result_nodes = []
        for group_model, app_model in group_list:
            group_dict = model_json.model_to_dict(group_model)
            app_dict = model_json.model_to_dict(app_model)
            node = NodeGroupInfo()
            node.id = "NodeGroupInfo_" + str(group_dict["id"])
            node.group_id = group_dict["group_id"]
            node.group_name = group_dict["group_name"]
            node.app_id = group_dict["app_id"]
            node.app_name = app_dict["app_name"]
            result_nodes.append(node)
    else:
        group_model, app_model = group_list
        group_dict = model_json.model_to_dict(group_model)
        app_dict = model_json.model_to_dict(app_model)
        node = NodeGroupInfo()
        node.id = "NodeGroupInfo_" + str(group_dict["id"])
        node.group_id = group_dict["group_id"]
        node.group_name = group_dict["group_name"]
        node.app_id = group_dict["app_id"]
        node.app_name = app_dict["app_name"]
        result_nodes = node
    return result_nodes


def fromTbInfoTelephone2NodeTelephoneInfo(tel_list):
    """

    :param tel_list: List<(TbInfoAppUser, TbInfoApp)>
    :return:
    """
    # result_dic = model_json.model_to_dict(app_user_list)
    if isinstance(tel_list, list):
        result_nodes = []
        for tel_model in tel_list:
            tel_dict = model_json.model_to_dict(tel_model)
            node = NodeTelephoneInfo()
            node.id = "NodeTelephoneInfo_" + str(tel_dict["id"])
            node.user_id = tel_dict["user_id"]
            node.telephone = tel_dict["telephone"]
            result_nodes.append(node)
    else:
        tel_dict = model_json.model_to_dict(tel_list)
        node = NodeTelephoneInfo()
        node.id = "NodeTelephoneInfo_" + str(tel_dict["id"])
        node.user_id = tel_dict["user_id"]
        node.telephone = tel_dict["telephone"]
        result_nodes = node
    return result_nodes


# Relations
def fromTbInfoAppUser2RelationAppUser(app_user_list):
    # TbInfoAppUser

    if isinstance(app_user_list, list):
        result_nodes = []
        for app_user_model in app_user_list:
            app_user = model_json.model_to_dict(app_user_model)
            relation = RelationAppUser()
            relation.id = "RelationAppUser_" + str(app_user["id"])
            relation.from_user = "NodeUserInfo_" + str(app_user["user_id"])
            relation.to_app = "NodeAppUserInfo_" + str(app_user["app_id"])
            result_nodes.append(relation)
    else:
        app_user = model_json.model_to_dict(app_user_list)
        relation = RelationAppUser()
        relation.id = "RelationAppUser_" + str(app_user["id"])
        relation.from_user = "NodeUserInfo_" + str(app_user["user_id"])
        relation.to_app = "NodeAppUserInfo_" + str(app_user["app_id"])
        result_nodes = relation
    return result_nodes


def fromTbDelivery2RelationDeliveryRecord(delivery_list):
    # RelationDeliveryRecord

    if isinstance(delivery_list, list):
        result_nodes = []
        for delivery_record in delivery_list:
            relation = RelationDeliveryRecord()
            relation.id = "RelationDeliveryRecord_" + str(delivery_record[0])
            relation.from_user_id = "NodeUserInfo_" + str(delivery_record[1])
            relation.to_user_id = "NodeUserInfo_" + str(delivery_record[2])

            relation.records = str(delivery_record[3])
            result_nodes.append(relation)
    else:
        delivery_record = delivery_list
        relation = RelationDeliveryRecord()
        relation.id = "RelationDeliveryRecord_" + str(delivery_record[0])
        relation.from_user_id = "NodeUserInfo_" + str(delivery_record[1])
        relation.to_user_id = "NodeUserInfo_" + str(delivery_record[2])
        relation.records = str(delivery_record[3])
        result_nodes = relation
    return result_nodes


def fromTbSearch2RelationSearchRecord(search_list):
    # TbSearch
    if isinstance(search_list, list):
        result_nodes = []
        for search_record in search_list:
            relation = RelationSearchRecord()
            relation.id = "RelationSearchRecord_" + str(search_record[0])
            relation.from_app_user_id = "NodeAppUserInfo_" + str(search_record[1])
            relation.to_search_id = "NodeSearchInfo_" + str(search_record[2])
            relation.records = str(search_record[3])
            result_nodes.append(relation)
    else:
        search_record = search_list
        relation = RelationSearchRecord()
        relation.id = "RelationSearchRecord_" + str(search_record[0])  # appuserid
        relation.from_app_user_id = "NodeAppUserInfo_" + str(search_record[1])
        relation.to_search_id = "NodeSearchInfo_" + str(search_record[2])
        relation.records = str(search_record[3])
        result_nodes = relation
    return result_nodes


def fromTbInfoGroupUser2RelationUserAppGroup(user_app_group_list):
    # TbInfoGroupUser
    if isinstance(user_app_group_list, list):
        result_nodes = []
        for user_app_group_model in user_app_group_list:
            user_app_group = model_json.model_to_dict(user_app_group_model)
            relation = RelationUserAppGroup()
            relation.id = "RelationUserAppGroup_" + str(user_app_group["id"])
            relation.from_app_user_id = "NodeAppUserInfo_" + str(user_app_group["app_user_id"])
            relation.to_app_group_id = "NodeGroupInfo_" + str(user_app_group["group_id"])
            relation.contents = str([
                {
                    'content': '购买甲醇',
                    'keywords': '甲醇',
                    'record_datetime': '2022-08-11 18:10:30'
                }
            ])
            result_nodes.append(relation)
    else:
        user_app_group = model_json.model_to_dict(user_app_group_list)
        relation = RelationUserAppGroup()
        relation.id = "RelationUserAppGroup_" + str(user_app_group["id"])
        relation.from_app_user_id = "NodeAppUserInfo_" + str(user_app_group["app_user_id"])
        relation.to_app_group_id = "NodeGroupInfo_" + str(user_app_group["group_id"])
        relation.contents = str([
            {
                'content': '购买甲醇',
                'keywords': '甲醇',
                'record_datetime': '2022-08-11 18:10:30'
            }
        ])
        result_nodes = relation
    return result_nodes


def fromTbInfoTelephone2RelationTelephoneInfo(tel_list):
    # TbInfoTelephone
    if isinstance(tel_list, list):
        result_nodes = []
        for user_tel_model in tel_list:
            user_app_group = model_json.model_to_dict(user_tel_model)
            relation = RelationTelephoneInfo()
            relation.id = "RelationTelephoneInfo_" + str(user_app_group["id"])
            relation.from_user_id = "NodeUserInfo_" + str(user_app_group["user_id"])
            relation.to_telephone_id = "NodeTelephoneInfo_" + str(user_app_group["id"])
            result_nodes.append(relation)
    else:
        user_app_group = model_json.model_to_dict(tel_list)
        relation = RelationTelephoneInfo()
        relation.id = "RelationTelephoneInfo_" + str(user_app_group["id"])
        relation.from_user_id = "NodeUserInfo_" + str(user_app_group["user_id"])
        relation.to_telephone_id = "NodeTelephoneInfo_" + str(user_app_group["id"])
        result_nodes = relation
    return result_nodes


def fromTbContentPersonal2RelationPersonalContent(content_list):
    # TbContentPersonal
    if isinstance(content_list, list):
        result_nodes = []
        for personal_content_model in content_list:
            # user_app_group = model_json.model_to_dict(personal_content_model)
            relation = RelationPersonalContent()
            relation.id = "RelationPersonalContent_" + str(personal_content_model[0])
            relation.from_app_user_id = "NodeAppUserInfo_" + str(personal_content_model[1])
            relation.to_app_user_id = "NodeAppUserInfo_" + str(personal_content_model[2])
            relation.contents = str(personal_content_model[3])
            result_nodes.append(relation)
    else:
        personal_content_model = content_list
        relation = RelationPersonalContent()
        relation.id = "RelationPersonalContent_" + str(content_list[0])
        relation.from_app_user_id = "NodeAppUserInfo_" + str(personal_content_model[1])
        relation.to_app_user_id = "NodeAppUserInfo_" + str(personal_content_model[2])
        relation.contents = str(personal_content_model[3])
        result_nodes = relation
    return result_nodes


def fromTbTelephoneRecord2RelationTelephoneRecord(tel_record_list):
    """

    :param tel_record_list: List< [from_telephone_id+to_telephone_id, from_telephone_id, to_telephone_id, List(record_datetime) ] >
    :return:
    """
    # TbTelephoneRecord
    if isinstance(tel_record_list, list):
        result_nodes = []
        for tel_record in tel_record_list:
            # user_app_group = model_json.model_to_dict(user_tel_model)

            relation = RelationTelephoneRecord()
            relation.id = "RelationTelephoneRecord_" + str(tel_record[0])
            relation.from_telephone_id = "NodeTelephoneInfo_" + str(tel_record[1])
            relation.to_telephone_id = "NodeTelephoneInfo_" + str(tel_record[2])
            relation.records = str(tel_record[3])
            result_nodes.append(relation)
    else:
        tel_record = tel_record_list
        relation = RelationTelephoneRecord()
        relation.id = "RelationTelephoneRecord_" + str(tel_record[0])
        relation.from_telephone_id = "NodeTelephoneInfo_" + str(tel_record[1])
        relation.to_telephone_id = "NodeTelephoneInfo_" + str(tel_record[2])
        relation.records = tel_record[3]
        result_nodes = relation
    return result_nodes


if __name__ == '__main__':
    Session = MysqlConnect("10.66.10.234:3306", "root", "234").connect("final")
    print(json.dumps([1, 2, 3]))

    # fromTbContentPersonal2RelationPersonalContent
    # l = UserService(Session).get_all_personal_content()
    # res = fromTbContentPersonal2RelationPersonalContent(l)
    # for i in res:
    #     print(i.__dict__)
    #     break

    # # test fromTbTelephoneRecord2RelationTelephoneRecord
    # l = UserService(Session).get_all_user_telephone_record()
    # res = fromTbTelephoneRecord2RelationTelephoneRecord(l)
    # for i in res:
    #     print(i.__dict__)
    #     break

    # # test fromTbInfoGroupUser2RelationUserAppGroup
    l = UserService(Session).get_all_group_user()
    res = fromTbInfoGroupUser2RelationUserAppGroup(l)
    for i in res:
        print(i.__dict__)
        # break

    # # test fromTbTelephoneRecord2RelationTelephoneRecord
    # user_tel_list_models = UserService(Session).get_all_user_telephone_record()
    # user_tel_list_edges = fromTbTelephoneRecord2RelationTelephoneRecord(user_tel_list_models)
    # for i in user_tel_list_edges:
    #     print(i.__dict__)
    #     break

    # test fromTbInfoTelephone2RelationTelephoneInfo
    # user_tel_list_models = UserService(Session).get_all_user_telephones()
    # user_tel_list_edges = fromTbInfoTelephone2RelationTelephoneInfo(user_tel_list_models)
    # for i in user_tel_list_edges:
    #     print(i.__dict__)
    #     break

    # # test fromTbInfoUser2NodeUserInfo
    # user_list = UserService(Session).get_all_user()
    # # print(user_list[0])
    # r_node = fromTbInfoUser2NodeUserInfo(user_list[0:2])
    # for i in r_node:
    #     print(i.__dict__)

    # test fromTbInfoAppUser2NodeAppUserInfo
    # app_user_list = UserService(Session).get_all_app_groups()
    # r_node = fromTbInfoGroup2NodeGroupInfo(app_user_list[0:2])
    # for i in r_node:
    #     print(i.__dict__)

    # app_user_list = UserService(Session).get_all_user_telephones()
    # r_node = fromTbInfoTelephone2NodeTelephoneInfo(app_user_list[0:2])
    # for i in r_node:
    #     print(i.__dict__)
    # print(app_user_list)
    # print(app_user_list[5][1].__dict__,app_user_list[5][1])
    # print(app_user_list[5][1].__dict__,app_user_list[5][1])

    # r_node = fromTbInfoAppUser2NodeAppUserInfo(app_user_list[0:2])
    # node_tag = r_node[0].__class__.__name__

    # 'INSERT VERTEX t2 (name, age) VALUES "11":("n1", 12);'
    # nosql = 'INSERT VERTEX {} ( '.format(node_tag)
    # values_list = ''
    # for i, node in enumerate(r_node):
    #     values = ''
    #     nid = ''  # sample "11":(
    #     for k, v in node.__dict__.items():
    #         if k == "id":
    #             nid = '"{}":('.format(v)
    #         if i == 0:
    #             nosql += (k + ",")
    #         if type(v) == str:
    #             values += '"{}",'.format(v)
    #         else:
    #             values += '{},'.format(v)
    #     values = (nid + values[:-1] + " ), ")
    #     values_list += values
    # nosql = (nosql[:-1] + " ) VALUES ")
    # nosql += (values_list[:-1] + ";")
    #
    # print(nosql)
    # print(values)
    # for i in r_node:
    #     print(i.__NodeName__)
