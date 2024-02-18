import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config
from driver.chrome_driver_factory import ChromeDriverFactory


class TestChromeDriverFactory:
    driver = None

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup_class(cls):
        TestChromeDriverFactory.driver = ChromeDriverFactory.create_chrome_driver()
        yield
        TestChromeDriverFactory.driver.close()
        TestChromeDriverFactory.driver.quit()

    def test_get_chrome_options(self):
        # Arrange
        expected_page_load_strategy = 'normal'
        expected_disable_extensions = True
        expected_use_automation_extension = False

        # Act
        chrome_options = ChromeDriverFactory.get_chrome_options()

        # Assert
        assert chrome_options.page_load_strategy == expected_page_load_strategy
        assert chrome_options.accept_insecure_certs == expected_disable_extensions
        assert chrome_options.experimental_options.get('useAutomationExtension') == expected_use_automation_extension

    def test_start_chrome_driver(self):
        # Assert driver is not None
        assert TestChromeDriverFactory.driver is not None
        config_instance = Config("linux")
        # Navigate to the URL
        TestChromeDriverFactory.driver.get("https://www.loblaws.ca/")
        TestChromeDriverFactory.driver.maximize_window()

        # Wait for elements to be present
        wait = WebDriverWait(TestChromeDriverFactory.driver, config_instance.get_pause_in_test())
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".logo")))
        wait.until(EC.presence_of_element_located((By.ID, "site-content")))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.booking-selector")))

        # Assert text of a specific element
        element = TestChromeDriverFactory.driver.find_element(By.CSS_SELECTOR, "div.booking-selector")
        assert element.text == "Glen Erin Drive".upper()

    @classmethod
    def test_create_chrome_driver(cls):
        # Assert
        assert isinstance(TestChromeDriverFactory.driver, webdriver.Chrome)
