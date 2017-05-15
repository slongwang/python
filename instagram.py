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
        desired_caps['deviceName'] = '4517d47e'
        desired_caps['appPackage'] = 'com.instagram.android'
        desired_caps['appActivity'] = '.activity.MainTabActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_like(self):
        WIDTH = self.driver.get_window_size()['width']
        HEIGHT = self.driver.get_window_size()['height']
        tabs = self.driver.find_elements_by_id("com.instagram.android:id/tab_icon")
        tabs[1].click()
        time.sleep(1)
        imgs = self.driver.find_elements_by_class_name("android.widget.ImageView")
        imgs[5].click()

        time.sleep(1)
        likes = self.driver.find_elements_by_id("com.instagram.android:id/row_feed_button_like")
        for i in range(1,100):
            try:
                for j in range(0,1):
                    if likes[j].is_selected() == False:
                        likes[j].click()
                        time.sleep(1)
            except :
                print 'next'
            self.driver.swipe(WIDTH / 2, HEIGHT * 5 / 6, WIDTH * 2 / 3, HEIGHT / 6, 1000)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)