import time

from selenium import webdriver
from selenium.webdriver.chrome import service

from selenium.webdriver.common.by import By

operapath = r"C:\Users\Tadin\Downloads\operadriver_win64\operadriver_win64\operadriver.exe"

webdriver_service = service.Service(operapath)
webdriver_service.start()

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Users\Tadin\AppData\Local\Programs\Opera GX\107.0.5045.75\opera.exe"
options.add_experimental_option('w3c', True)

driver = webdriver.Remote(webdriver_service.service_url, options=options)

driver.get('https://google.com')
