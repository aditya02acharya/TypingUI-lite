import unittest

from api.aiagent.device.touchscreendevice import TouchScreenDevice


class DeviceTestCase(unittest.TestCase):

    data = {
            "name": "finnish keyboard",
            "layout_file": "api/aiagent/config/finnish_layout.npy"
    }

    def test_layout_loading_correct(self):
        """
        Check if function loads layout when
        path is correct
        """
        device = TouchScreenDevice(self.data)

        self.assertTrue(device.load_layout(self.data["layout_file"]))

    def test_layout_loading_wrong(self):
        """
        Check if function loads layout when
        path is incorrect
        """
        device = TouchScreenDevice(self.data)

        self.assertFalse(device.load_layout(None))
