import os

import flask_jwt_extended
import yaml
from flask_mail import Message


def load_yaml_file(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f.read())


def load_config_from_yaml_file(config_file):
    if not os.path.isabs(config_file):
        raise Exception('The configuration file MUST be specified using an absolute path.')
    config = load_yaml_file(config_file)
    return config


def update_config_from_environment(config):
    for key in config:
        config[key] = os.environ.get(key, config[key])
    return config


def load_config(from_file=None, env=True):
    config = {}
    if from_file is not None:
        config = load_config_from_yaml_file(from_file)
    if env:
        return update_config_from_environment(config)
    return config


def decode_token(token):
    if token and token.startswith('Bearer '):
        return flask_jwt_extended.decode_token(token[7:])
    else:
        return flask_jwt_extended.decode_token(token)


def send_email(mail, message, recipients, html):
    msg = Message(message,
                  sender=("Discover Quests", "email@example.com"),
                  recipients=recipients)
    msg.html = html
    mail.send(msg)
