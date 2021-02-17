import os
import logging
from .utilities.logging_config_manager import setup_logging


def init_log_config():
    # Setup Logger.
    if not os.path.isdir("logs"):
        # if logs folder doesn't exist create one.
        os.makedirs("logs")
    setup_logging(default_path=os.path.join("config", "logging.yml"))
    logger = logging.getLogger(__name__)
    logger.info("logger is set.")
