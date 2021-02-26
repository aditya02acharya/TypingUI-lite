import pytest

from api.aiagent.device.touchscreendevice import TouchScreenDevice

@pytest.fixture
def device_object():
    device_config = {
        "layout_file": "api/aiagent/config/finnish_layout.npy"
    }
    device = TouchScreenDevice(device_config)
    return device

@pytest.fixture
def device_config():
    config = {
        "name": "finnish keyboard",
        "layout_file": "api/aiagent/config/finnish_layout.npy"
    }

    return config

def test_layout_loading_correct(device_object, device_config):
    status = device_object.load_layout(device_config["layout_file"])
    assert status == True

def test_layout_loading_worng(device_object, device_config):
    status = device_object.load_layout("finnish_layout.npy")
    assert status == False

def test_layout_loading_none(device_object, device_config):
    status = device_object.load_layout(None)
    assert status == False

def test_layout_loading_empty(device_object, device_config):
    status = device_object.load_layout("")
    assert status == False

def test_get_coordinate_correct(device_object):
    coor = device_object.get_coordinate("g")
    assert (1 in coor[0] and 4 in coor[1]) == True

def test_get_coordinate_empty(device_object):
    coor = device_object.get_coordinate("")
    assert (coor[0].size == 0 and coor[1].size == 0) == True

def test_get_coordinate_none(device_object):
    coor = device_object.get_coordinate(None)
    assert (coor[0].size == 0 and coor[1].size == 0) == True

def test_get_character_correct(device_object):
    character = device_object.get_character(1, 4)
    assert character == 'g'

def test_get_character_float(device_object):
    character = device_object.get_character(1.0, 4.0)
    assert character == ''

def test_get_character_none(device_object):
    character = device_object.get_character(None, 4.0)
    assert character == ''

def test_get_character_boundry(device_object):
    character = device_object.get_character(5, 12)
    assert character == ''

def test_random_key(device_object):
    character = device_object.get_random_key()
    assert ((character >= 'a' and character <= 'z') or 
    character == ' ' or character == '<' or 
    character == 'ö' or character == 'ä' or character == 'å') == True