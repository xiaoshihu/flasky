from flask import Blueprint

# 蓝本到底是个什么东西？为什么需要在每个pkg里面都生成一个蓝本，不能用一个蓝本吗
auth = Blueprint('auth', __name__)

from . import views
