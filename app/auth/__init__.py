from flask import Blueprint

auth = Blueprint('auth', __name__)

# 認証関連のビュー関数(ルート)をインポート
from . import views
