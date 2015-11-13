# -*- coding: utf-8 -*-

def screenshot(driver,path):
    driver.get_screenshot_as_file(path)