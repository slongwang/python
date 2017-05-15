#!/usr/bin/python
# coding=utf-8
import os
from time import sleep
import time
import unittest

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.2'
        desired_caps['deviceName'] = '4732de4c'
        desired_caps['appPackage'] = 'sg.bigo.live'
        desired_caps['appActivity'] = 'com.yy.iheima.startup.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_like(self):
        WIDTH = self.driver.get_window_size()['width']
        HEIGHT = self.driver.get_window_size()['height']
        time.sleep(3)
        lives = self.driver.find_elements_by_id("sg.bigo.live:id/iv_show")
        lives[0].click()
        for i in range(1,100):
            self.driver.swipe(WIDTH / 2, HEIGHT * 5 / 6, WIDTH * 2 / 3, HEIGHT / 6, 1000)
            time.sleep(2)
            self.driver


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)