from selenium import webdriver


class ChromeDriverFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_chrome_options():
        # Configure Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.accept_insecure_certs = True
        chrome_options.page_load_strategy = 'normal'
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_experimental_option('useAutomationExtension', False)
        return chrome_options

    @staticmethod
    def create_chrome_driver():
        # Create the ChromeDriver instance with the service and options
        service = webdriver.ChromeService()
        driver = webdriver.Chrome(service=service, options=ChromeDriverFactory.get_chrome_options())
        return driver

    @staticmethod
    def create_remote_chrome_driver(self, hub):
        chrome_options = ChromeDriverFactory.get_chrome_options()
        # Create a remote WebDriver instance
        driver = webdriver.Remote(command_executor=hub, options=chrome_options)
        return driver

