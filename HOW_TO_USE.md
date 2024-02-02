### From terminal 
```
>>>> from driver import chrome_driver_factory
>>> driver = chrome_driver_factory.ChromeDriverFactory()
>>> driver.create_chrome_driver()
<selenium.webdriver.chrome.webdriver.WebDriver (session="39ae677b369547ffcc5351325e641ffb")>
>>>
```
### From Console
```
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
>>> from driver import chrome_driver_factory
chrome = chrome_driver_factory.ChromeDriverFactory()
driver = chrome.create_chrome_driver()
driver.get('http://google.com')
driver.quit()
```
 

