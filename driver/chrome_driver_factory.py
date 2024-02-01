from selenium import webdriver

class ChromeDriverFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_chrome_driver(path_to_exec):
        chrome_options = ChromeDriverFactory.get_chrome_options()
        chrome_options.binary_location = path_to_exec
        return webdriver.Chrome(executable_path=path_to_exec, options=chrome_options)

    @staticmethod
    def create_remote_chrome_driver(hub):
        chrome_options = ChromeDriverFactory.get_chrome_options()
        return webdriver.Remote(command_executor=hub, desired_capabilities=chrome_options.to_capabilities())

    @staticmethod
    def get_chrome_driver_path():
        # You can replace this with your own logic to get the Chrome driver path
        # For example, using the Config class from your previous code
        return '/path/to/chromedriver'

    @staticmethod
    def get_chrome_options():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.accept_insecure_certs = True
        chrome_options.page_load_strategy = 'normal'
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_experimental_option('useAutomationExtension', False)
        return chrome_options