import logging


class InfoFilter(logging.Filter):
    """
    Simple Filter class
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__(name='filter_info_logs')

    def filter(self, record):
        """
        Return Log Record Object based on condition - Return only info logs

        Args:
        -----
            record: Log Record Object

        Return:
        -------
            record: Log Record Object
        """
        assert isinstance(record, logging.LogRecord)
        if record.levelno == logging.INFO:
            return record


class DebugFilter(logging.Filter):
    """
    Simple Filter class
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__(name='filter_debug_logs')

    def filter(self, record):
        """
        Return Log Record Object based on condition - Return only debug logs

        Args:
        -----
            record: Log Record Object

        Return:
        -------
            record: Log Record Object
        """
        assert isinstance(record, logging.LogRecord)
        if record.levelno == logging.DEBUG:
            return record
