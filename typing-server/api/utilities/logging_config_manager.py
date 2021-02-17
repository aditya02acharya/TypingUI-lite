import os
import logging
import logging.config
import sys
import yaml

"""
This function is used to setup root logging configuration,
* If LOG_CFG variable is set, then use it for logging configuration path.
* Since we are using yaml configuration, use yaml module to load file.
* Set Root logger configuration using `logging.config.dictConfig()`.
* Any exception results in setting up root logger in default configuration.
"""


# Function to configure root logger
def setup_logging(default_path='logging.yaml',
                  default_level=logging.INFO,
                  env_key='LOG_CFG'):
    """
    Logging Setup

    Args:
    -----
        default_path: Logging configuration path.
        default_level: Default logging level.
        env_key: Logging config path set in environment variable.
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value

    if os.path.exists(path):
        with open(path, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
            except Exception as e:
                print('Failed to load logging.yml. Using default configs.', e)
                logging.basicConfig(level=default_level, stream=sys.stdout)
    else:
        logging.basicConfig(level=default_level, stream=sys.stdout)
        print('Failed to find logging.yaml. Using default configs')
