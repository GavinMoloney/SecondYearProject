import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class test_NavLinks(unittest.TestCase):
    my_chrome_browser = ""
    my_firefox_browser = ""
    app_url = ""

    def setUp(self):
        self.my_chrome_browser = webdriver.Chrome()

        self.app_url = "http://127.0.0.1:8000/"
        self.my_chrome_browser.get(self.app_url)
        self.my_chrome_browser.implicitly_wait(2)

        if self.my_chrome_browser.current_url != self.app_url:
            print("Wrong page loaded, please check")
        else:
            print("AstroShop Home Page Loaded")

    def test_shopNavLink_inChrome(self):

        shop_link = self.my_chrome_browser.find_element_by_link_text("SHOP")
        shop_link.click()

        assert "http://127.0.0.1:8000/shop/" in self.my_chrome_browser.current_url

        success1 = self.my_chrome_browser.find_element_by_name("q")
        if success1:
            print("Shop Search Element Found - On Shop Page")
        else:
            print("Not on shop page")
        """
        success2 = self.my_chrome_browser.find_element_by_partial_link_text("/store")
        if success2:
            print("On Shop Page")
        else:
            print("Not on shop page")
        """

    def test_galleryNavLink_inChrome(self):
        gallery_link = self.my_chrome_browser.find_element_by_link_text("GALLERY")
        gallery_link.click()

        assert "http://127.0.0.1:8000/gallery/" in self.my_chrome_browser.current_url

        success2 = self.my_chrome_browser.find_element_by_class_name('text-white')
        if success2:
            print("Gallery class name found - On Gallery Page")
        else:
            print("Not on gallery page")

    def test_contactNavLink_inChrome(self):
        contact_link = self.my_chrome_browser.find_element_by_link_text("CONTACT")
        contact_link.click()

        assert "http://127.0.0.1:8000/contact" in self.my_chrome_browser.current_url

        success3 = self.my_chrome_browser.find_element_by_id("div_id_your_email")
        if success3:
            print("ID found - On Contact Page")
        else:
            print("Not on contact page")

    def tearDown(self):
        self.my_chrome_browser.close()
        print("Test script executed successfully.")
        time.sleep(4)
        self.my_chrome_browser.quit()

    print("All Successful")