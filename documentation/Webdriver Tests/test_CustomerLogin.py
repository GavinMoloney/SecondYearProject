import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class test_CustomerLogin(unittest.TestCase):
    my_chrome_browser = ""
    my_firefox_browser = ""
    app_url = ""

    def setUp(self):
        self.my_chrome_browser = webdriver.Chrome()
        # self.my_firefox_browser = webdriver.Firefox()

        self.app_url = "http://127.0.0.1:8000/login/"

        self.my_chrome_browser.get(self.app_url)
        self.my_chrome_browser.implicitly_wait(2)
        # self.my_firefox_browser.get(self.app_url)
        # self.my_firefox_browser.implicitly_wait(2)

    def test_customerLoginSuccessfully_inChrome(self):
        if self.my_chrome_browser.current_url != self.app_url:
            print("Wrong page loaded, please check")
        else:
            print("AstroShop Login Page Loaded")
            userid_element = self.my_chrome_browser.find_element_by_name("username")
            userid_element.clear()
            password_element = self.my_chrome_browser.find_element_by_name("password")
            password_element.clear()

            if userid_element.is_displayed() and password_element.is_displayed():
                userid_element.send_keys("Gmoloney")
                password_element.send_keys("Ruffian23")
                button_element = self.my_chrome_browser.find_element_by_css_selector(".btn.btn-secondary")
                button_element.click()

                assert "http://127.0.0.1:8000/" in self.my_chrome_browser.current_url
                print("Login Successful")
            else:
                print("Wrong elements used, correct them")

    def tearDown(self):
        self.my_chrome_browser.close()
        print("Test script executed successfully.")
        time.sleep(4)
        self.my_chrome_browser.quit()


