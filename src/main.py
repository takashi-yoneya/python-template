import datetime
import logging
import os

from pydantic import BaseModel

from common.configs import configs
from common.logger import init_logger
from sub import sub_func

# loggerの初期化
init_logger(configs.LOGGER_CONFIG_PATH)

logger = logging.getLogger(__name__)


class User(BaseModel):
    id: int
    name: str
    job: str


def main() -> None:
    logger.info("Start main")
    logger.info(f"{datetime.datetime.now(tz=datetime.timezone.utc)=}")
    logger.info(f'{os.path.join("src", "main.py")=}')
    logger.info(f'{sub_func(text="Hello World!")=}')
    user = User(id=1, name="Takashi Yoneya", job="Software Engineer")
    logger.info(user)
    logger.warning("This is warning message.")
    logger.error("This is error message.")
    try:
        1 / 0  # noqa
    except Exception as e:
        logger.exception(e)
    logger.info("End main")


if __name__ == "__main__":
    main()
