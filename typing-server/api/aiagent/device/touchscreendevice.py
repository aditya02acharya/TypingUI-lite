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
            self.logger.error('None value found for file path')
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
    
    def get_coordinate(self, char):
        """
        Returns the (row, column) index corresponding to the character.

        Args:
        -----
            char: target character to find the coordinates for.
        
        Return:
        -------
            coord: tuple representing ndarray row and ndarray col of character.
        """
        coord = np.where(self.layout == char)

        return coord
    
    def get_character(self, row, column):
        """
        Returns the string character corresponding to the (row, column).
        :param row: int value of the row.
        :param column: int value of the column.
        :return: string character.
        """

        if row is None or column is None:
            self.logger.error('row {%s} or column {%s} is None' % (str(row), str(column)))
            return ''
        
        if not type(row) == int or not type(column) == int:
            self.logger.error('row {%s} or column {%s} does not match type int' % (str(type(row)), str(type(column))))
            return ''

        if 0 <= row < self.layout.shape[0] and 0 <= column < self.layout.shape[1]:
            return self.layout[row][column]
        else:
            self.logger.error('row {%d} or column {%d} is out of bound' % (row, column))
            return ''
    

    def get_random_key(self):
        """
        Returns a random string character present in the layout.

        Return:
        -------
            target: a target character to press.
        """

        return np.random.choice(self.keys, 1, replace=True)

    def initialise_sensor_position(self):
        """
        Initialise the sensor position on the screen.

        Return:
        -------
            coord: list with random row and column.
        """
        random_row = np.random.randint(0, self.layout.shape[0])
        random_column = np.random.randint(0, self.layout.shape[1])

        self.logger.debug('setting the sensor to row {%d} and column {%d}' % (random_row, random_column))
        return [random_row, random_column]

    def start(self):
        """
        Function to initialise the device.

        Return:
        -------
            sensor_loc: list with random row and column.
            target_key: a target character to press.
        """

        self.logger.debug('Starting the touch screen device.')

        # Initialise the sensor position to a random location.
        sensor_loc = self.initialise_sensor_position()
        target_key = self.get_random_key()

        return sensor_loc, target_key
