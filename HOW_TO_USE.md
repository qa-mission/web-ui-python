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
### Run pyu
```
pavel@pavel-nata:~/QAMISSION/workspace/python/master/web-ui-python$ pytest tests/config/config_tests.py 
=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.10.12, pytest-8.0.0, pluggy-1.4.0
rootdir: /home/pavel/QAMISSION/workspace/python/master/web-ui-python
collected 3 items                                                                                                                                                                                                 

tests/config/config_tests.py ...                                                                                                                                                                            [100%]

================================================================================================ 3 passed in 0.01s ================================================================================================
pavel@pavel-nata:~/QAMISSION/workspace/python/master/web-ui-python$ 
```

Note: python consider "user.dir" differently than java. Because of that, the
test has the following line:
```
import os
import sys
import pytest

sys.path.insert(0,'/home/pavel/QAMISSION/workspace/python/master/web-ui-python')

from config.config import Config
from utils.ini_files_reader import IniFilesReader
```