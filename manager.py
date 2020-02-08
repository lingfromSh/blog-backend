import os

from flask import Flask

from .config.base import Config
from .config.dev import config as config_dev
from .config.pro import config as config_pro
from dataclasses import dataclass
from .user import user


@dataclass
class Manager:
    name = "Application Manager"
    version = "0.1"
    config: Config
    app: Flask


if os.environ.get("FLASK_MODE") == "dev":
    manager = Manager(config_dev, Flask(__name__))
else:
    manager = Manager(config_pro, Flask(__name__))

app = manager.app
app.register_blueprint(user, url_prefix="/user")
