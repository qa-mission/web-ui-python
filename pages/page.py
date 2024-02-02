from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from config.config import Config


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=Config.get_config().get_pause_in_test())

    def get_all_regexp_from(self, input_text, regexp):
        pattern = re.compile(regexp)
        matches = pattern.findall(input_text)
        return matches

    def scroll_to_the_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    def scroll_to_the_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def move_to_locator(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.move_to_element(element)

    def move_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def scroll_to_locator(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.scroll_to_element(element)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.wait.until(EC.visibility_of(element))

    def scroll_to_point(self, point):
        x = point.x
        y = point.y
        script = f"window.scrollTo({x},{y});"
        self.driver.execute_script(script)

    def scroll_by_pixels(self, length):
        command = f"window.scrollBy(0,{length})"
        self.driver.execute_script(command)

    def contains_text(self, text):
        return text in self.driver.page_source

    def pause(self, millis):
        time.sleep(millis)
