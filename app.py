from flask import Flask, jsonify

from service.Mysql.db_connector import MysqlConnect
from service.NebulaGraph.nebula_connector import NebulaConnector

# app = Flask(__name__)
# Session = MysqlConnect("8.130.78.75:3306", "root", "123456").connect("final")
Session = MysqlConnect("10.66.10.234:3306", "root", "234").connect("final")


connection_pool = NebulaConnector("10.66.10.234", 9669, "root", "nebula").connect()


# @app.route('/', methods=['GET'])
# def print_hi():
#     connection_pool = NebulaConnector("10.66.10.234", 9669, "root", "nebula").connect()
#     with connection_pool.session_context("root", "nebula") as ng_session:
#         ng_session.execute("USE basketball")
#         result = ng_session.execute('MATCH p=(v:player{name:"Tim Duncan"})-->(v2) RETURN p')
#         result_to_df(result)
#     # connection_pool.close()
#     print(111)
#     return jsonify(333)


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     app.run(debug=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
