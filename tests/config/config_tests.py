import os
import sys

import pytest

sys.path.insert(0,'/home/pavel/QAMISSION/workspace/python/master/web-ui-python')
from config.config import Config
from utils.ini_files_reader import IniFilesReader


# Replace 'your_module' with the actual module where your classes are located.

# Define a fixture to create an instance of IniFilesReader
@pytest.fixture
def ini_files_reader():
    reader = IniFilesReader()
    return reader

# Define a fixture to create an instance of Config
@pytest.fixture
def config():
    config_instance = Config("linux")
    return config_instance


def test_ini_files_reader_load_ini_file(ini_files_reader):
    # Create a temporary .ini file for testing
    with open("test_file.ini", "w") as file:
        file.write("key1=value1\nkey2=value2")

    # Load the temporary .ini file
    ini_files_reader.load_ini_file("test_file.ini")

    # Check if the values are loaded correctly
    assert ini_files_reader.get_value("key1") == "value1"
    assert ini_files_reader.get_value("key2") == "value2"

    # Clean up the temporary file
    os.remove("test_file.ini")


def test_config_get_chrome_driver_path(config):
    # Check if the chrome driver path is correctly retrieved
    chrome_driver_path = config.get_chrome_driver_path()
    expected_path = os.path.join(os.getcwd(), "resources/drivers/chromedriver")
    assert chrome_driver_path == expected_path


def test_config_get_pause_in_test(config):
    # Check if the pause in test duration is correctly retrieved
    pause_duration = config.get_pause_in_test()
    assert pause_duration == 15000  # Replace with the expected value

# You can add more test cases as needed.
