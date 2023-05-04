import os
from pathlib import Path

from pydantic import BaseSettings


class Configs(BaseSettings):
    """全体で使用するConfig情報を一元管理するためのClass
    環境毎に異なる設定は.envに記述して読み込む
    全環境で共通の設定は、以下に直接記述する
    """

    ENV: str
    VERSION: str = "0.0.1"
    SRC_DIR_PATH: str = os.path.join(
        Path(__file__).parent.parent.absolute()
    )  # srcディレクトリの絶対パス
    LOGGER_CONFIG_PATH: str = os.path.join(
        SRC_DIR_PATH, "logger_config.yaml"
    )  # loggerの設定ファイルのパス

    class Config:
        # .envファイルを読み込む
        env_file = ".env"
        env_file_encoding = "utf-8"


configs = Configs()
