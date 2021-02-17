import logging


class FingerAgentEnv:

    def __init__(self, conf):
        """
        Finger Environment class simulates finger movement on
        touchscreen keyboard.

        Args:
        -----
            conf: disctionary object consisting of configurations
                  for device.

        """

        self.logger = logging.getLogger(__name__)
