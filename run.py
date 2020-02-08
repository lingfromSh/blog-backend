import datetime  # time
import os  # environment
import subprocess
import typing

import fire  # cli

WORKDIR = os.environ.get("PWD", None)  # 当前目录
HOST_NAME = os.environ.get("BLOG_HOST", "0.0.0.0")  # blog host name
HOST_PORT = os.environ.get("BLOG_HOST_PORT", 8000)  # blog host port
MODE = {"dev": "开发", "pro": "生产"}

if WORKDIR is None:
    print("未知路径. 启动失败")
    exit(1)


def start(mode: typing.AnyStr):
    """开发模式:
    1. 默认开启Flask DEBUG模式
    2. 日志提示显示debug信息
    """
    mode = MODE.get(mode, "dev")
    print(f"\033[0;31m[INFO]\033[m [{datetime.datetime.now()}] 开启\033[0;36m{mode}\033[m模式")
    print(
        f"\033[0;31m[INFO]\033[m [{datetime.datetime.now()}] 设置Flask配置文件路径: \033[0;36m{WORKDIR}/config/{mode}.py\033[m"
    )
    # app mode
    os.environ["FLASK_MODE"] = mode
    # flask main app path
    os.environ["FLASK_APP"] = f"{WORKDIR}/manager:app"
    # use development mode
    os.environ["FLASK_ENV"] = "development"
    subprocess.run(f"flask run -h {HOST_NAME} -p {HOST_PORT}".split())


if __name__ == "__main__":
    fire.Fire()
