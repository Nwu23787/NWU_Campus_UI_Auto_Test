import os.path
import logging
import logging.handlers

# 测试项目基地址
BASE_PATH = os.path.dirname(__file__)
# 被测项目基URL
BASE_URL = "http://127.0.0.1:3000"
# 首页URL
INDEX_URL = BASE_URL + "/index"
# 注册页URL
ADMIN_URL = BASE_URL + "/register"
# 登录页URL
LOGIN_URL = BASE_URL + "/login"
# 发表话题页
TOPIC_URL = BASE_URL + "/addTopic"


def set_log_config():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(level=logging.INFO)
    # 创建处理器
    lf = logging.handlers.TimedRotatingFileHandler(filename=BASE_PATH + '/log/tp_test.log', when='midnight', interval=1,
                                                   backupCount=2, encoding="utf8")
    ls = logging.StreamHandler()
    # 创建格式器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt=fmt)
    # 将格式器添加到处理器
    ls.setFormatter(formatter)
    lf.setFormatter(formatter)
    # 将处理器添加到日志器
    logger.addHandler(ls)
    logger.addHandler(lf)
