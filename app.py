from flask import Flask, jsonify, request

from service.Mysql.UserService import UserService
from service.Mysql.db_connector import MysqlConnect
from service.NebulaGraph.controller import Controller
from service.NebulaGraph.nebula_connector import NebulaConnector
from utils import model_json, Response
from flask_cors import CORS
app = Flask(__name__)
# Session = MysqlConnect("8.130.78.75:3306", "root", "123456").connect("final")

CORS(app)
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
@app.route('/get_path_by_card_id', methods=['GET'])
def get_path_by_car_id():
    """
    Wg6iJHcszX
    :return:
    """
    card_id = request.args.get("card_id")
    c = Controller("test_final", ng_connection_pool)
    r = c.get_n_r_by_card_id(card_id, rootID=True)
    return Response.ResponseData(Response.CodeNumber.Success, "success", r).to_json()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
    # Session = MysqlConnect("10.66.10.234:3306", "root", "234").connect("final")
    #
    # r = UserService(Session).get_personal_app_info()
    # print(model_json.model_to_dict(r))
    # print('*' * 30)
    # r = UserService(Session).get_telephone_record()
    # print(r)
    # print(model_json.model_to_dict(r))
    # print(model_to_dict(r))
