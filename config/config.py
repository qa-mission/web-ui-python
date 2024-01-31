import os
import sys
from utils.IniFilesReader import IniFilesReader


class Config:
    _instance = None

    @classmethod
    def get_config(cls, env_name):
        if cls._instance is None:
            cls._instance = cls(env_name)
        return cls._instance

    def __init__(self, env_name):
        self.reader = IniFilesReader()
        self.env = env_name
        if self.env is None:
            print("env is not provided. Please set environment variable 'env'")
            sys.exit(-1)

        self.root_path = os.getenv('ROOT', os.getcwd())
        self.resources_path = f"{self.root_path}/resources"

        self.read_properties(f"{self.resources_path}/etc")
        self.read_properties(f"{self.resources_path}/env/{self.env}")

    def read_properties(self, prop_path):
        self.reader.load_ini_files(prop_path)

    def get_chrome_driver_path(self):
        return f"{self.resources_path}/drivers/{self.reader.get_value('chromeDriverExec')}"

    def get_pause_in_test(self):
        return int(self.reader.get_value('PAUSE_IN_TEST_MILLS'))

    def get_user_name(self):
        return self.reader.get_value('pc_user_name')

    def get_user_password(self):
        return self.reader.get_value('pc_user_password')
