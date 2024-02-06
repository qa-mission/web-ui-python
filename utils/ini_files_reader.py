import os


class IniFilesReader:
    def __init__(self):
        self.data = {}

    def load_ini_files(self, root_folder):
        for dirpath, dirnames, filenames in os.walk(root_folder):
            for filename in filenames:
                if filename.endswith(".ini"):
                    ini_file_path = os.path.join(dirpath, filename)
                    self.load_ini_file(ini_file_path)

    def load_ini_file(self, ini_file_path):
        with open(ini_file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    self.data[key] = value

    def get_value(self, key):
        return self.data.get(key, None)
