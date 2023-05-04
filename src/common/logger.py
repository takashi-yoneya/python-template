from logging.config import dictConfig

import yaml


def init_logger(filepath: str) -> None:
    with open(filepath) as f:
        config = yaml.safe_load(f)
        dictConfig(config)
