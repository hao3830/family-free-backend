import yaml
from easydict import EasyDict


def parse_yaml(path):
    with open(path, "r") as f:
        data = yaml.safe_load(f)

    return EasyDict(data)


def _get_config(path):
    config = parse_yaml(path)
    return config


def get_config():
    return _get_config("configs/app.yaml")


def get_db_config():
    return _get_config("configs/database.yaml")


def get_service_config():
    return _get_config("configs/service.yaml")


def get_security_config():
    return _get_config("configs/security.yaml")
