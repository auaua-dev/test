from flask import Flask
from src.util.path_manager import TEMPLATE_FOLDER, STATIC_FOLDER, LOGS_FOLDER

# # ログ出力の設定
# import logging
# from flask.logging import default_handler

# 静的ファイルの設定
# from static_folder import rsc, bootstrap, vue
# from favicon import favicon_bp

# Blueprintの設定
from ud_top import ud
# from nsu02_select_inspection_target import nsu02
# from nsu03_execute_inspection import nsu03
# from nsu05_change_sensitivity import nsu05
# from nsu06_search_inspection_history import nsu06
# from nsu07_confirm_inspection_history import nsu07
# from nsu09_confirm_error_log import nsu09

app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)

# 静的ファイルの設定
# app.register_blueprint(rsc)
# app.register_blueprint(bootstrap)
# app.register_blueprint(vue)
# app.register_blueprint(favicon_bp)

# ログ出力の設定
# logger_werkzeug = logging.getLogger('werkzeug')
# filehandler = logging.FileHandler(filename=str(LOGS_FOLDER) + '/web_access.log')
# logger_werkzeug.addHandler(default_handler)
# logger_werkzeug.addHandler(filehandler)

# Blueprintの設定
app.register_blueprint(ud)
# app.register_blueprint(nsu02)
# app.register_blueprint(nsu03)
# app.register_blueprint(nsu05)
# app.register_blueprint(nsu06)
# app.register_blueprint(nsu07)
# app.register_blueprint(nsu09)

# 起動モードの設定（下記の設定は開発環境用となっている）
# app.config.from_object('config.DebugMode')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
