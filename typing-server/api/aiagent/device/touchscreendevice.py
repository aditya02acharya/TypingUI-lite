import logging
import numpy as np
from os import path


class TouchScreenDevice():
    def __init__(self, device_config, ignore_key='-'):
        """
        Touchscreen device class. Consist of Device state
        and few utility functions.

        Args:
        -----
            device_config: dictionary consisting of device
                           configurations.
            ignore_key: symbol to represent keys on keyboard
                        to ignore.
        """

        self.logger = logging.getLogger(__name__)
        self.layout = None

        self.load_layout(device_config.get("layout_file", None))
        unique_list = np.unique(self.layout)
        self.keys = np.delete(unique_list, np.where(unique_list == ignore_key))

    def load_layout(self, layout_file):
        """
        Function to load keyboard layout from file.

        Args:
        -----
            layout_file: path to saved layout file on disk.
        """

        if layout_file is None:
            self.logger.error('None value found for file path')clear
            return False

        if path.exists(layout_file):
            try:
                self.layout = np.load(layout_file)
                self.logger.debug('device layout loading completed.')
                return True
            except Exception as e:
                self.logger.error('failed to load file: {%s}.' % str(e))
        else:
            self.logger.error('failed to load layout file {%s}.' % layout_file)

        return False
