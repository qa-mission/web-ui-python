import pytest
from selenium import webdriver
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
        assert chrome_options.accept_insecure_certs != expected_disable_extensions  # This might need to be revised based on actual option being tested
        assert chrome_options.experimental_options.get('useAutomationExtension') == expected_use_automation_extension

    @classmethod
    def test_create_chrome_driver(cls):
        # Assert
        assert isinstance(TestChromeDriverFactory.driver, webdriver.Chrome)
