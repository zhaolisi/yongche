#coding=utf-8
from selenium import webdriver
import ConfigParser
import os
from framework.logger import Logger

logger = Logger(logger='BrowserEngine').getlog()

class BrowserEngine():
    chrome_driver_dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = chrome_driver_dir + '/tools/chromedriver'
    def __init__(self,driver):
        self.dirver = driver
    def open_browser(self,driver):
        config = ConfigParser.ConfigParser()
        configpath = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(configpath)
        browser = config.get('browserType', 'browserName')
        logger.info("You had select %s browser." % browser)
        url = config.get('testServer', 'URL')
        logger.info("The test server url is: %s" % url)
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")

