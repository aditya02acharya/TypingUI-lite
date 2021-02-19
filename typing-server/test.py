import unittest

from api import init_log_config
from tests.api.aiagent.device_test import DeviceTestCase

if __name__ == "__main__":
    init_log_config()
    DeviceTestCase()
    unittest.main()
