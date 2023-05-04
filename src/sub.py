import logging

logger = logging.getLogger(__name__)


def sub_func(text: str) -> str:
    logger.info("sub_func")
    return f"sub_func: {text}"


def example() -> None:
    logger.info("example")
