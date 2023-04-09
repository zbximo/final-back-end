from flask import Flask, jsonify

from service.Mysql.UserService import UserService
from service.Mysql.db_connector import MysqlConnect
from service.NebulaGraph.nebula_connector import NebulaConnector
from utils import model_json

# app = Flask(__name__)
# Session = MysqlConnect("8.130.78.75:3306", "root", "123456").connect("final")


ng_connection_pool = NebulaConnector("10.66.10.234", 9669, "root", "nebula").connect()

# @app.route('/', methods=['GET'])
# def print_hi():
#     ng_connection_pool = NebulaConnector("10.66.10.234", 9669, "root", "nebula").connect()
#     with ng_connection_pool.session_context("root", "nebula") as ng_session:
#         ng_session.execute("USE basketball")
#         result = ng_session.execute('MATCH p=(v:player{name:"Tim Duncan"})-->(v2) RETURN p')
#         result_to_df(result)
#     # ng_connection_pool.close()
#     print(111)
#     return jsonify(333)
# @app.route('/', methods=['GET'])
# def print_hi():

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(1)
    # app.run(debug=True)
    # Session = MysqlConnect("10.66.10.234:3306", "root", "234").connect("final")
    #
    # r = UserService(Session).get_personal_app_info()
    # print(model_json.model_to_dict(r))
    # print('*' * 30)
    # r = UserService(Session).get_telephone_record()
    # print(r)
    # print(model_json.model_to_dict(r))
    # print(model_to_dict(r))
